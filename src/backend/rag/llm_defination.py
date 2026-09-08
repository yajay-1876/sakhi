from langchain_groq import ChatGroq
def get_llm():
    return ChatGroq(model="openai/gpt-oss-120b", temperature=0)


# from langchain_openai import ChatOpenAI
# def get_llm():
#     return ChatOpenAI(model="gpt-4o-mini", temperature=0)
