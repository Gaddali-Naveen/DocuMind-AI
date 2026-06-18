from langchain_chroma import Chroma

from app.embeddings.embedding_model import load_embedding_model
from app.llm.groq_model import load_llm
from app.prompting.prompt_builder import build_prompt


chat_history = []

embedding_model = None
vector_store = None
llm = None


def initialize():

    global embedding_model
    global vector_store
    global llm

    if embedding_model is None:

        embedding_model = load_embedding_model()

    if vector_store is None:

        vector_store = Chroma(
            persist_directory="vector_db",
            embedding_function=embedding_model
        )

    if llm is None:

        llm = load_llm()


def ask_question(question):

    initialize()

    retrieved_docs = vector_store.similarity_search(
        question,
        k=2
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

    chat_history.append(f"User: {question}")
    chat_history.append(f"Assistant: {response.content}")

    return response.content, retrieved_docs


if __name__ == "__main__":

    print("\nDocuMind AI Started")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("Ask a Question: ")

        if question.lower() == "exit":
            break

        answer, docs = ask_question(question)

        print("\nAnswer:\n")
        print(answer)

        print("\nSources:\n")

        unique_sources = set()

        for doc in docs:
            unique_sources.add(doc.metadata["source"])

        for source in unique_sources:
            print(source)

        print("\n" + "=" * 60 + "\n")