#-------------setup logger-----------------------#

from src.logger_config.logger_config import setup_logger
import logging
setup_logger()
logger=logging.getLogger(__name__)
#------------------------------------------------#

from langchain_groq import ChatGroq

from src.db.crud import add_message, get_chat_history_by_conv_id

llm=ChatGroq( model="llama-3.3-70b-versatile" )

def ask_answer_service(conv_id, user_query):
    try:
        add_message(conv_id=conv_id, role="user", content=str(user_query))
        chat_history=get_chat_history_by_conv_id(conv_id) or []

        llm_response=llm.invoke(chat_history)
        answer=str(llm_response.content)
        add_message(conv_id=conv_id, role="assistant", content=answer)
        response={
            "answer":answer
        }
        logger.info(f"Response :{response['answer']}")
        return response

    except Exception as e:
        logger.error(f"Error in ask_answer_service :{e}")
        raise

# response=ask_answer_service("271d11b5-6c5e-44b6-8682-0d2c58edaeea","what is my my first question in this chat")
# print(response["answer"])