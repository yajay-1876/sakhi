#-------------setup logger-----------------------#
from src.logger_config.logger_config import setup_logger
import logging
setup_logger()
logger=logging.getLogger(__name__)
#------------------------------------------------#
import hashlib
from fastapi import UploadFile

from src.db.crud import add_document
from src.backend.rag.pipeline import process_pdf

async def document_upload_service(conv_id: str, file: UploadFile):
    try:
        # Read Complete File
        file_bytes= await file.read()

        # Generate SHA-256 hash
        document_id= hashlib.sha256(file_bytes).hexdigest()
        logger.info(f"Generated document id: {document_id}")
        filename=file.filename or "UntitledDoc.pdf"

        is_doc_added_to_pg = add_document(document_id, conv_id, filename)
        if is_doc_added_to_pg:
            logger.info(f"{filename} uploaded successfully.")
            result = process_pdf(file_bytes, document_id, conv_id, filename)
            if result["success"]:
                logger.info(f"Document with {result['chunks_count']} chunks , Upserted to Pinecone.")
                return {
                    "status" : True,
                    "chunks" : result["chunks_count"]
                }
        if not is_doc_added_to_pg:
            return {
                "status"  : False,
                "message" : "Document already exists"
            }

    except Exception :
        logger.exception(f"Failed to upsert document to pinecone.")
        raise