from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

llm = ChatGroq( model="openai/gpt-oss-20b" )

title_prompt = PromptTemplate(
    input_variables=["user_query"],
    template="""
You are an expert at creating chat titles.

Generate a concise conversation title.

Rules:
- Maximum 4 words.
- Use title case.
- No punctuation.
- No quotation marks.
- No prefixes such as "Title:".
- Do not repeat the question.
- Summarize the main topic.
- Do not invent information.
- Return ONLY the title.

User Query:
{user_query}

Title:
""",
)

title_chain = title_prompt | llm


def get_title(user_query: str) -> str:
    """
    Generate a short conversation title from the user's first query.
    """

    response = title_chain.invoke( {"user_query": user_query} )

    return response.content.strip()



# user_query="what is python"
# print(f"user_query : {user_query}")
# print(get_title(user_query))