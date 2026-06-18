from langchain_huggingface import HuggingFaceEmbeddings


def load_embedding_model():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings


if __name__ == "__main__":

    embedding_model = load_embedding_model()

    sample_text = "Employees receive 18 annual leave days."

    vector = embedding_model.embed_query(sample_text)

    print(f"\nVector Length: {len(vector)}")

    print("\nFirst 10 Values:")

    print(vector[:10])