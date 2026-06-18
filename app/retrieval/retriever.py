from langchain_chroma import Chroma

from app.embeddings.embedding_model import load_embedding_model


def load_vector_store():

    embedding_model = load_embedding_model()

    vector_store = Chroma(
        persist_directory="vector_db",
        embedding_function=embedding_model
    )

    return vector_store


if __name__ == "__main__":

    vector_store = load_vector_store()

    query = "How many annual leaves are provided?"

    results = vector_store.similarity_search(
        query,
        k=2
    )

    print("\nRetrieved Chunks:\n")

    for doc in results:

        print(doc.page_content)

        print("\nMetadata:")

        print(doc.metadata)

        print("_" * 50)