import streamlit as st

from app.llm.groq_model import load_llm
from app.prompting.prompt_builder import build_prompt


chat_history = []

llm = None


def initialize():

    global llm

    if llm is None:
        llm = load_llm()


def ask_question(question):

    initialize()

    if "vector_store" not in st.session_state:
        return (
            "⚠️ Please upload documents and click '🚀 Process Documents' first.",
            []
        )

    vector_store = st.session_state["vector_store"]

    retrieved_docs = vector_store.similarity_search(
        question,
        k=3
    )

    if not retrieved_docs:
        return (
            "No relevant information was found in the uploaded documents.",
            []
        )

    retrieved_context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    history = "\n".join(chat_history)

    full_context = f"""
Previous Conversation:
{history}

Retrieved Context:
{retrieved_context}
"""

    prompt = build_prompt(
        question=question,
        context=full_context
    )

    response = llm.invoke(prompt)

    chat_history.append(
        f"User: {question}"
    )

    chat_history.append(
        f"Assistant: {response.content}"
    )

    return response.content, retrieved_docs


if __name__ == "__main__":

    print("\nDocuMind AI Started")
    print("Use Streamlit UI to interact.\n")