#-------------setup logger-----------------------#
from src.logger_config.logger_config import setup_logger
import logging
setup_logger()
logger=logging.getLogger(__name__)
#------------------------------------------------#

from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, UploadFile, File, Form

from src.backend.services.document_upload_service import document_upload_service

router=APIRouter(
    prefix="/document",
    tags=["DOCUMENT"]
)

@router.post("/upload")
async def document_upload(
        conv_id:str = Form(...),           # The ... (Ellipsis) means: This field is required.
        uploaded_file: UploadFile = File(...)
    ):
    logger.info(f"Document Upload {uploaded_file.filename}")
    try:
        return await document_upload_service(conv_id, uploaded_file)
    except Exception as e:
        logger.error(f"Failed to response from get_user_service.py : {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
