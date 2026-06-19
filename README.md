# 🧠 DocuMind AI

### Enterprise Document Intelligence Assistant powered by LangChain, FAISS, Groq & Hugging Face

DocuMind AI is an end-to-end Retrieval-Augmented Generation (RAG) application that enables users to upload documents and interact with them through natural language conversations. The system processes PDF, DOCX, and TXT files, generates vector embeddings, retrieves relevant context using semantic search, and provides accurate answers using a Large Language Model.

---

## 🚀 Live Demo

🌐 https://documentai-assistant-l5wrzbxtxckpaajqxgylet.streamlit.app/

---

## ✨ Features

* 📄 Upload TXT, PDF, and DOCX documents
* 🔍 Semantic Search using FAISS Vector Store
* 🤖 AI-Powered Question Answering with Groq LLM
* 🧠 Conversational Memory Support
* 📚 Retrieval-Augmented Generation (RAG)
* ⚡ Fast Document Processing
* 🌐 Interactive Streamlit Web Interface
* ☁️ Deployed on Streamlit Cloud
* 📂 Multi-Document Support
* 🔗 Source Document Tracking

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
Hugging Face Embeddings
          │
          ▼
FAISS Vector Store
          │
          ▼
Retriever
          │
          ▼
Groq LLM (Llama 3.3 70B)
          │
          ▼
Final Response
```

## 🛠️ Tech Stack

### AI & RAG

* LangChain
* FAISS
* Hugging Face Embeddings
* Groq (Llama 3.3 70B)

### Frontend

* Streamlit

### Programming Language

* Python

### Document Processing

* PyPDF
* Docx2txt

---

## 📂 Supported Document Types

* TXT Files
* PDF Files
* DOCX Files

---

## 📸 Application Preview

Upload documents and ask questions directly from your knowledge base.

Example Queries:

* Summarize the leave policy
* Explain employee benefits
* What is the travel reimbursement process?
* What are the onboarding guidelines?

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

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
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

## 📁 Project Structure

```text
DocuMind-AI
│
├── app
│   ├── embeddings
│   ├── frontend
│   ├── ingestion
│   ├── llm
│   ├── prompting
│   ├── vectorstore
│   ├── rag_pipeline.py
│
├── data
│
├── requirements.txt
│
├── README.md
│
└── .env
```

---

## 🎯 Use Cases

* Enterprise Knowledge Base
* HR Policy Assistant
* Internal Documentation Search
* Employee Support Assistant
* Customer Support Knowledge Retrieval
* Company Document Q&A

---

## 📈 Future Enhancements

* Multi-User Authentication
* Chat Export Feature
* Conversation Persistence
* Hybrid Search (FAISS + BM25)
* Source Highlighting
* PDF Page-Level Citations
* Cloud Storage Integration

---

## 👨‍💻 Author

**Gaddali Naveen Babu**

Final Year B.Tech (Artificial Intelligence & Data Science)

Passionate about AI Engineering, Retrieval-Augmented Generation (RAG), LLM Applications, and Intelligent Systems.

GitHub:
https://github.com/Gaddali-Naveen

LinkedIn:
https://www.linkedin.com/in/gaddali-naveen-babu/

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
