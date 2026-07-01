#-------------setup logger-----------------------#
from src.logger_config.logger_config import setup_logger
import logging
setup_logger()
logger=logging.getLogger(__name__)
#------------------------------------------------#

from src.backend.services.utils.get_title import get_title
from src.db.crud import create_new_conversation

def create_conv_service(user_id, user_query):
    title=get_title(user_query)
    conv_id=create_new_conversation(user_id, title)
    response={
        "conv_id":conv_id,
        "title":title
    }
    logger.info(f"Response :{response}")
    return response