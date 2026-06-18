from pathlib import Path

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    Docx2txtLoader
)


def load_documents(folder_path):

    documents = []

    # TXT Files
    for file in Path(folder_path).glob("*.txt"):

        loader = TextLoader(str(file))

        documents.extend(loader.load())

    # PDF Files
    for file in Path(folder_path).glob("*.pdf"):

        loader = PyPDFLoader(str(file))

        documents.extend(loader.load())

    # DOCX Files
    for file in Path(folder_path).glob("*.docx"):

        loader = Docx2txtLoader(str(file))

        documents.extend(loader.load())

    return documents


if __name__ == "__main__":

    docs = load_documents("data")

    print(f"\nLoaded Documents: {len(docs)}\n")

    for doc in docs:

        print(doc.metadata)

        print("-" * 50)