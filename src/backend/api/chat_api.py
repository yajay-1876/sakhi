#-------------setup logger-----------------------#
from src.logger_config.logger_config import setup_logger
import logging
setup_logger()
logger=logging.getLogger(__name__)
#------------------------------------------------#

from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

from src.backend.services.ask_answer_service import ask_answer_service

router=APIRouter(
    prefix="/chat",
    tags=["CHAT"]
)

# FastAPI receives JSON, not a Python dictionary.
class AskAnswerRequest(BaseModel):
    conv_id    : str
    user_query : str
@router.post("/ask")
def ask_answer_api(request: AskAnswerRequest):
    logger.info(f"conv_id:{request.conv_id} ; user_query:{request.user_query}")
    try:
        response=ask_answer_service(request.conv_id, request.user_query)
        return response
    except Exception as e:
        logger.error(f"Failed to response from get_user_service.py : {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
