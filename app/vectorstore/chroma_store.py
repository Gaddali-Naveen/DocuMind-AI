from langchain_chroma import Chroma

from app.ingestion.loader import load_documents
from app.ingestion.chunker import create_chunks
from app.embeddings.embedding_model import load_embedding_model


def create_vector_store():

    docs = load_documents("data")

    chunks = create_chunks(docs)

    embedding_model = load_embedding_model()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return vector_store


if __name__ == "__main__":

    st.session_state.vector_store = create_vector_store()

    print("\nVector Store Created Successfully!")

    print(
        f"Total Chunks Stored: {vector_store._collection.count()}"
    )