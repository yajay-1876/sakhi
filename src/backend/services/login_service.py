#-------------setup logger-----------------------#
from src.logger_config.logger_config import setup_logger
import logging
setup_logger()
logger=logging.getLogger(__name__)
#------------------------------------------------#

from src.db.crud import create_or_get_userid

def get_user_service(username):
    user_id=create_or_get_userid(username)
    response={
        "user_id":user_id,
        "username":username
    }
    logger.info(f"Response :{response}")
    return response