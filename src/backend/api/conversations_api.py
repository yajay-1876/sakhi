#-------------setup logger-----------------------#
from src.logger_config.logger_config import setup_logger
import logging
setup_logger()
logger=logging.getLogger(__name__)
#------------------------------------------------#

from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

from src.backend.services.create_conv_service import create_conv_service
from src.db.crud import get_conversations_by_user
from src.db.crud import get_chat_history_by_conv_id

router=APIRouter(
    prefix="/conversations",
    tags=["CONVERSATIONS"]
)

# FastAPI receives JSON, not a Python dictionary.
class CrateConversationRequest(BaseModel):
    user_id  : str
    user_query : str
@router.post("/create")
def create_conv_api(request: CrateConversationRequest):
    logger.info(f"create_conv_api ; user_id:{request.user_id} UserQuery:{request.user_query}")
    try:
        response=create_conv_service(request.user_id, request.user_query)
        return response
    except Exception as e:
        logger.error(f"Failed to response from get_conv_service.py : {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))



# FastAPI receives JSON, not a Python dictionary.
class GetAllConversationsRequest(BaseModel):
    user_id  : str
@router.post("/get_all_conv")
def get_all_conv_api(request: GetAllConversationsRequest):
    logger.info(f"get_all_conv_api ; user_id :{request.user_id}")
    try:
        response=get_conversations_by_user(request.user_id)
        return response
    except Exception as e:
        logger.error(f"Failed to response from get_conv_service.py : {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


# FastAPI receives JSON, not a Python dictionary.
class GetChatHistoryRequest(BaseModel):
    conv_id  : str
@router.post("/get_chat_history")
def get_chat_history_api(request: GetChatHistoryRequest):
    logger.info(f"get_chat_history ; conv_id:{request.conv_id}")
    try:
        response=get_chat_history_by_conv_id(request.conv_id)
        return response
    except Exception as e:
        logger.error(f"Failed to response from get_conv_service.py : {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
