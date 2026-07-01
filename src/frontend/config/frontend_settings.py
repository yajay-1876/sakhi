from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    BACKEND_URL:str

    class Config:
        env_file=".env"
        env_file_encoding="utf-8"
        extra="allow"