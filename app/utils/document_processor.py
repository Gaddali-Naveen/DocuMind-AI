from pathlib import Path
import shutil

from app.vectorstore.chroma_store import create_vector_store


DATA_FOLDER = "data"
VECTOR_DB = "vector_db"


def save_uploaded_files(uploaded_files):

    Path(DATA_FOLDER).mkdir(exist_ok=True)

    for file in uploaded_files:

        file_path = Path(DATA_FOLDER) / file.name

        with open(file_path, "wb") as f:

            f.write(file.getbuffer())


def rebuild_vector_store():

    if Path(VECTOR_DB).exists():

        shutil.rmtree(VECTOR_DB)

    vector_store = create_vector_store()

    return vector_store._collection.count()