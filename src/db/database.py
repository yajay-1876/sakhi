from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
load_dotenv()
from src.db.config.db_settings import DBSettings
settings=DBSettings()
DATABASE_URL=settings.DATABASE_URL

engine=create_engine(
    url=DATABASE_URL,
    pool_pre_ping=True
)


SessionLocal=sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass










"""
sessionmaker()
      ↓
SessionLocal
      ↓
db = SessionLocal()
      ↓
db.add()
      ↓
db.commit()
      ↓
PostgreSQL
"""
"""
pool_pre_ping=True

Before SQLAlchemy gives you a connection from its connection pool, it runs a lightweight test query to verify the connection is still alive.

Without it:

Connection was idle for a long time
↓
Postgres closes it
↓
SQLAlchemy tries to reuse it
↓
OperationalError

With it:

Connection requested
↓
SQLAlchemy sends ping
↓
If dead → creates new connection
↓
Returns valid connection

Useful for:

Streamlit apps
FastAPI apps
Long-running services
"""
