from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.ingestion.loader import load_documents


def create_chunks(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    return chunks


if __name__ == "__main__":

    docs = load_documents("data")

    chunks = create_chunks(docs)

    print(f"\nTotal Chunks: {len(chunks)}\n")

    for i, chunk in enumerate(chunks, start=1):

        print(f"Chunk {i}")

        print(chunk.page_content)

        print("\nMetadata:")

        print(chunk.metadata)

        print("_" * 50)