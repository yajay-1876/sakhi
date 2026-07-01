from langchain_groq import ChatGroq
def get_llm():
    return ChatGroq(model="llama-3.3-70b-versatile", temperature=0)


# from langchain_openai import ChatOpenAI
# def get_llm():
#     return ChatOpenAI(model="gpt-4o-mini", temperature=0)
