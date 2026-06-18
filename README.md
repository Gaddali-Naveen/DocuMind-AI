# DocuMind-AI
Built DocuMind-AI, a Retrieval-Augmented Generation (RAG) powered document assistant.

# 🧠 DocuMind AI

Turn Documents into Conversations with AI.

DocuMind AI is an intelligent Retrieval-Augmented Generation (RAG) application that allows users to upload documents and ask natural language questions. The system retrieves relevant information from the uploaded documents and generates accurate responses using Groq LLMs.

---

## 🚀 Features

* 📄 Upload TXT, PDF, and DOCX files
* 🔍 Semantic Search using ChromaDB
* 🧠 HuggingFace Embeddings
* ⚡ Groq LLM Integration
* 💬 Conversational Chat Interface
* 📚 Multi-Document Question Answering
* 📝 Source Citation Display
* 🎨 Modern Streamlit UI
* 🔄 Automatic Vector Store Creation

---

## 🏗️ Architecture

```text
User Uploads Documents
           │
           ▼
Document Loader
           │
           ▼
Text Chunking
           │
           ▼
HuggingFace Embeddings
           │
           ▼
ChromaDB Vector Store
           │
           ▼
Retriever
           │
           ▼
Groq LLM
           │
           ▼
Final Answer + Sources
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### LLM

* Groq

### Embeddings

* HuggingFace Sentence Transformers

### Vector Database

* ChromaDB

### Framework

* LangChain

---

## 📂 Project Structure

```text
DocuMind-AI
│
├── app
│   ├── embeddings
│   ├── frontend
│   ├── ingestion
│   ├── llm
│   ├── memory
│   ├── prompting
│   ├── retrieval
│   ├── vectorstore
│   └── rag_pipeline.py
│
├── data
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Gaddali-Naveen/DocuMind-AI.git
cd DocuMind-AI
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run Application

```bash
streamlit run app/frontend/app.py
```

---

## 📸 Demo Questions

* What is the password policy?
* How many annual leave days are provided?
* Can annual leave be carried forward?
* What health benefits are available?
* What is the remote work policy?

---

## 🎯 Future Improvements

* Hybrid Search (BM25 + Vector Search)
* Conversation Persistence
* User Authentication
* Cloud Deployment
* Multi-User Support
* Document Management Dashboard

---

## 👨‍💻 Author

**Gaddali Naveen**

B.Tech Artificial Intelligence & Data Science

Aspiring AI Engineer | GenAI Enthusiast | Data Engineer

---

⭐ If you found this project useful, consider giving it a star.
