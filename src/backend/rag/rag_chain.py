from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

from src.backend.rag.retriever import retrieve_chunks
from src.backend.rag.llm_defination import get_llm

llm=get_llm()

RAG_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a RAG assistant.

Use only the supplied book context to answer the user's question.

Rules:
- Use only the provided context.
- Do not use your own knowledge.
- Use chat history only to understand follow-up questions.
- Do NOT mention source information throughout the answer.
- After completing the answer, add a separate section titled "Sources".
- Under "Sources", list each source document only once.
- For each source document, include all relevant page numbers.
- If multiple pieces of information come from the same document, combine the page numbers instead of repeating the document name.
- Do not invent filenames or page numbers. Use only those present in the supplied context.
- Print page numbers in intergers . Do not use float values.
"""
        ),
        (
            "human",
            """
Book Context:
{context}

Chat History:
{chat_history}

Question:
{question}
"""
        ),
    ]
)
RAG_chain = RAG_PROMPT | llm | StrOutputParser()
def ask_rag_question(context, chat_history, question):

    answer = RAG_chain.invoke(
        {
            "context": context,
            "chat_history": chat_history,
            "question": question,
        }
    )
    return answer




CHAT_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are Sakhi, a helpful AI assistant.

Answer the user's question using the conversation history when relevant.

Do not mention documents, context, page numbers, filenames, or sources unless the user explicitly asks for them.
"""
        ),
        (
            "human",
            """
Chat History:
{chat_history}

Question:
{question}
"""
        ),
    ]
)
chain = CHAT_PROMPT | llm | StrOutputParser()
def ask_question(chat_history, question):

    answer = chain.invoke(
        {
            "chat_history": chat_history,
            "question": question,
        }
    )
    return answer