from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from fastapi import FastAPI
from src.backend.api import routers
app= FastAPI(title="Sakhi API")

for router in routers:
    app.include_router(router)

from src.backend.config.backend_settings import Settings
settings=Settings()

if __name__=="__main__":
    import uvicorn
    uvicorn.run("src.backend.main:app", host=settings.API_HOST, port=settings.API_PORT)
