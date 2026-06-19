import sys
from pathlib import Path

import streamlit as st

project_root = Path(__file__).resolve().parents[2]

if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from app.rag_pipeline import ask_question
from app.vectorstore.faiss_store import create_vector_store


# --------------------------------------------------
# CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="DocuMind AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e293b 25%,
        #312e81 50%,
        #1e1b4b 75%,
        #0f172a 100%
    );
}

/* Main Title */
.big-title {
    text-align: center;
    font-size: 4rem;
    font-weight: 900;
    background: linear-gradient(
        90deg,
        #38bdf8,
        #818cf8,
        #c084fc,
        #ec4899
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #e5e7eb;
    font-size: 1.2rem;
    margin-bottom: 2rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #111827,
        #1f2937
    );
}

/* Chat Cards */
div[data-testid="stChatMessageContent"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.10);
    padding: 15px;
    border-radius: 18px;
    backdrop-filter: blur(12px);
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 12px;
    font-weight: bold;
    border: none;
    color: white;
    background: linear-gradient(
        90deg,
        #3b82f6,
        #8b5cf6
    );
}

/* File Upload */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.05);
    padding: 12px;
    border-radius: 12px;
}

/* Alerts */
[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Custom Card */
.custom-card {
    text-align:center;
    padding:15px;
    margin-bottom:25px;
    border-radius:15px;
    background:rgba(255,255,255,0.08);
    border:1px solid rgba(255,255,255,0.1);
}

/* Footer */
.footer {
    text-align:center;
    color:#9ca3af;
    font-size:14px;
    padding:15px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🚀 DocuMind AI")

    st.markdown("---")

    st.subheader("📚 Knowledge Base")

    uploaded_files = st.file_uploader(
        "Upload Documents",
        type=["txt", "pdf", "docx"],
        accept_multiple_files=True
    )

    if st.button("🚀 Process Documents"):

        if uploaded_files:

            Path("data").mkdir(exist_ok=True)

            for file in uploaded_files:

                file_path = Path("data") / file.name

                with open(file_path, "wb") as f:

                    f.write(file.getbuffer())

            with st.spinner("Creating Embeddings..."):

                st.session_state.vector_store = create_vector_store()

            st.success(
                "Documents Processed Successfully!"
            )

        else:

            st.warning(
                "Please upload at least one file."
            )

    st.markdown("---")

    st.subheader("✨ Features")

    st.success("TXT Support")
    st.success("PDF Support")
    st.success("DOCX Support")
    st.success("Groq LLM")
    st.success("FAISS Vector Store")
    st.success("Chat Memory")
    st.success("Dynamic Prompting")

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    """
<div class='big-title'>
🧠 DocuMind AI
</div>

<div class='subtitle'>
Turn Documents into Conversations
</div>
""",
    unsafe_allow_html=True
)

st.markdown("""
<div class="custom-card">

<h4 style="color:#38bdf8;">
📚 Upload • Search • Understand • Chat
</h4>

<p style="color:#d1d5db;">
Transform PDFs, DOCX and TXT files into an AI-powered knowledge base.
</p>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SESSION
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# CHAT HISTORY
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

question = st.chat_input(
    "Ask a question about your documents..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.spinner("🤖 Thinking..."):

        answer, docs = ask_question(question)

    sources = set()

    for doc in docs:

        if "source" in doc.metadata:
            sources.add(doc.metadata["source"])

    source_text = "\n".join(
        [
            f"• {source}"
            for source in sources
        ]
    )

    final_answer = f"""
{answer}

---
### 📄 Sources

{source_text}
"""

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": final_answer
        }
    )

    with st.chat_message("assistant"):

        st.markdown(final_answer)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<hr style="border:1px solid rgba(255,255,255,0.1);">

<div class="footer">

🧠 DocuMind AI v1.0

<br><br>

Built with ❤️ using LangChain • Groq • FAISS • Hugging Face • Streamlit

<br><br>

© 2026 DocuMind AI | Intelligent Document Understanding Platform

</div>
""", unsafe_allow_html=True)