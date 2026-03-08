# 📚 RAG Assistant – AI Document Question Answering Web App

An AI-powered **Retrieval-Augmented Generation (RAG) web application** that allows users to upload a PDF document and ask questions about its content. The system retrieves relevant document sections and generates accurate answers using a large language model.

This project demonstrates how to combine **vector databases, embeddings, and LLMs** to build an intelligent document assistant.

---

## 🚀 Features

* 📄 Upload PDF documents
* ❓ Ask questions about the document
* 🔍 Context-aware answers using RAG
* 🧠 AI responses powered by LLM
* 🗂 Vector storage for document chunks
* 🕘 Search history (last 10 questions)
* ⚡ Fast responses using optimized embeddings

---

## 🏗 Architecture

The application follows a **two-tier architecture**:

Frontend
→ Streamlit Web UI

Backend
→ FastAPI API server

AI Pipeline
→ Document Processing
→ Embedding Generation
→ Vector Database Retrieval
→ LLM Answer Generation

---

## 🧠 Technologies Used

* Python
* FastAPI (Backend API)
* Streamlit (Web Interface)
* LangChain (AI orchestration)
* ChromaDB (Vector Database)
* HuggingFace Embeddings
* Groq LLM (Llama 3.1 model)
* PyPDF (PDF processing)

---

## ⚙️ How It Works

1. User uploads a PDF document.
2. The backend extracts text from the PDF.
3. The text is split into smaller chunks.
4. Each chunk is converted into embeddings.
5. Embeddings are stored in a vector database.
6. When a user asks a question:

   * Relevant chunks are retrieved.
   * The LLM generates an answer using the retrieved context.

This method is called **Retrieval-Augmented Generation (RAG)**.

---

## 📂 Project Structure

```
RAG-Assistant/
│
├── app.py          # FastAPI backend
├── chat.py         # Streamlit frontend
├── chroma_db/      # Vector database storage
├── .env            # API keys
├── requirements.txt
└── README.md
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

You can get an API key from Groq.

---

## 📦 Installation

Clone the repository:

```
git clone https://github.com/FikirteGT/ISHUBworkshop_day5.git
cd rag-assistant
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the backend server:

```
uvicorn app:app --reload
```

Start the frontend:

```
streamlit run chat.py
```

Open your browser:

```
http://localhost:8501
```

---

## 🖥 Example Usage

1. Upload a PDF document.
2. Ask a question related to the document.
3. The system retrieves relevant sections.
4. The AI generates an answer.

---

## 📈 Future Improvements

* Multi-document support
* Conversational memory
* Highlight answer sources
* Chat-style interface
* Authentication and user sessions
* Deployment to cloud

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Acknowledgements

* LangChain
* ChromaDB
* Groq
* HuggingFace
* Streamlit
