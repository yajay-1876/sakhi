import os
from pinecone import Pinecone

from src.backend.config.backend_settings import Settings

settings= Settings()

pc = Pinecone(
    api_key=settings.PINECONE_API_KEY
)

index = pc.Index(
    settings.PINECONE_INDEX_NAME
)