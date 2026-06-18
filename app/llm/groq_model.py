from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

load_dotenv()


def load_llm():

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY")
    )

    return llm


if __name__ == "__main__":

    llm = load_llm()

    response = llm.invoke(
        "What is Artificial Intelligence?"
    )

    print(response.content)