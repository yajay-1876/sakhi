from pydantic_settings import BaseSettings
from pydantic import SecretStr
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    API_HOST:str ="localhost"
    API_PORT:int = 8000
    GROQ_API_KEY:SecretStr
    PINECONE_API_KEY:str
    PINECONE_INDEX_NAME:str

    class Config:
        env_file=".env"
        env_file_encoding="utf-8"
        extra="allow"
