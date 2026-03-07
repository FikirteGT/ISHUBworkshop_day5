import os
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq

load_dotenv()

app = FastAPI()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

# Remove the global retriever from startup
# retriever will be created inside /ask to always get latest docs

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)


class QuestionRequest(BaseModel):
    question: str


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    with open("temp.pdf", "wb") as f:
        f.write(await file.read())

    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    db.add_documents(chunks)

    return {"message": "Document uploaded successfully"}


@app.post("/ask")
def ask_question(request: QuestionRequest):

    # Create a new retriever here every time to include the latest uploaded PDFs
    retriever = db.as_retriever(search_kwargs={"k": 3})

    docs = retriever.invoke(request.question)

    context = ""
    for i, d in enumerate(docs):
        context += f"Source {i+1}:\n{d.page_content}\n\n"

    prompt = f"""
Answer only from the sources below.
If the answer is not in the document say: Not in document.

{context}

Question: {request.question}
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }
