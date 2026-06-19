from langchain_community.vectorstores import FAISS

from app.ingestion.loader import load_documents
from app.ingestion.chunker import create_chunks
from app.embeddings.embedding_model import load_embedding_model


def create_vector_store():

    print("Loading Documents...")

    docs = load_documents("data")

    print(f"Documents Loaded: {len(docs)}")

    chunks = create_chunks(docs)

    print(f"Chunks Created: {len(chunks)}")

    embedding_model = load_embedding_model()

    vector_store = FAISS.from_documents(
        chunks,
        embedding_model
    )

    print("FAISS Vector Store Created!")

    return vector_store


if __name__ == "__main__":

    vector_store = create_vector_store()

    print("Done!")