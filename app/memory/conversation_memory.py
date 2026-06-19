from langchain.memory import ConversationBufferMemory


def load_memory():

    memory = ConversationBufferMemory(
        return_messages=True
    )

    return memory