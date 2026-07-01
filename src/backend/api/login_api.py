#-------------setup logger-----------------------#
from src.logger_config.logger_config import setup_logger
import logging
setup_logger()
logger=logging.getLogger(__name__)
#------------------------------------------------#

from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

from src.backend.services.login_service import get_user_service

router=APIRouter(
    prefix="/auth",
    tags=["LOGIN"]
)

# FastAPI receives JSON, not a Python dictionary.
class LoginRequest(BaseModel):
    username: str

# Pydantic automatically creates python object .
# request_obj = LoginRequest("Subbu@1611")
@router.post("/login")
def login_api(request: LoginRequest):

    logger.info(f"Input Login UserName:{request.username}")
    try:
        response=get_user_service(request.username)
        return response
    except Exception as e:
        logger.error(f"Failed to response from get_user_service.py : {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
