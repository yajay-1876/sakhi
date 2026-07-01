"""
Run once (e.g. on app startup or as a migration script) to create all tables.

Usage:
    python -m db.init_db
    # or call init_db() from your app's lifespan / startup event.
"""

from src.db.database import engine , Base

from src.db import models            # Ensure all models are registered on same Base


def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database tables created (or verified) successfully.")
    print(Base.metadata.tables.keys())

if __name__=="__main__":
    init_db()