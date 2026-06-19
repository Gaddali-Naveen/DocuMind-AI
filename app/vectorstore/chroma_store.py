from langchain_chroma import Chroma

from app.ingestion.loader import load_documents
from app.ingestion.chunker import create_chunks
from app.embeddings.embedding_model import load_embedding_model


def create_vector_store():

    print("Loading Documents...")

    docs = load_documents("data")

    print(f"Total Documents Loaded: {len(docs)}")

    print("Creating Chunks...")

    chunks = create_chunks(docs)

    print(f"Total Chunks Created: {len(chunks)}")

    print("Loading Embedding Model...")

    embedding_model = load_embedding_model()

    print("Creating Chroma Vector Store...")

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    print("Vector Store Created Successfully!")

    return vector_store


if __name__ == "__main__":

    vector_store = create_vector_store()

    print(
        f"\nTotal Chunks Stored: "
        f"{vector_store._collection.count()}"
    )