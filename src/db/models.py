from datetime import datetime, timezone
def _now_utc()->datetime:
    return datetime.now(timezone.utc)

from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship

from src.db.database import Base

class User(Base):
    __tablename__= "users"

    id= Column(Text, primary_key=True)
    username= Column(Text, nullable=False , default="Unknown UserName", unique=True)
    created_at= Column(DateTime(timezone=True), nullable=False, default=_now_utc)

    conversations= relationship(
        "Conversation",
        back_populates="user",
        order_by="Conversation.last_interacted.desc()",
        cascade="all, delete-orphan"
    )

class Conversation(Base):
    __tablename__ = "conversations"

    id              = Column(Text, primary_key=True)
    user_id         = Column(Text, ForeignKey(column="users.id", ondelete="CASCADE"), nullable=False)
    title           = Column(Text, nullable=False, default="Untitled Conversation")
    last_interacted = Column(DateTime(timezone=True), nullable=False, default=_now_utc )

    messages = relationship(
        "Message",
        back_populates="conversation",
        order_by="Message.ts",          # Fetched messages appear Chronological in a conversation
        cascade="all, delete-orphan"
    )
    user= relationship(
        "User",
        back_populates="conversations"
    )
    documents=relationship(
        "Document",
        back_populates="conversation",
        order_by="Document.uploaded_at",
        cascade="all, delete-orphan"
    )
    __table_args__=(Index("ix_conversations_last_interacted", last_interacted.desc()),)

class Message(Base):
    __tablename__= "messages"

    id              = Column(Integer, primary_key=True, autoincrement=True)
    conversation_id = Column(Text, ForeignKey(column="conversations.id", ondelete="CASCADE"), nullable=False)
    role            = Column(Text, nullable=False)
    content         = Column(Text, nullable=False)
    ts              = Column(DateTime(timezone=True), nullable=False, default=_now_utc)

    conversation =relationship(
        "Conversation",
        back_populates="messages"
    )

class Document(Base):
    __tablename__ = "documents"

    id= Column(Text, primary_key=True)
    document_id=Column(Text, nullable=False)
    conversation_id= Column(Text, ForeignKey(column="conversations.id",  ondelete="CASCADE"), nullable=False)
    filename= Column(Text, nullable=False)
    uploaded_at= Column(DateTime(timezone=True), nullable=False, default=_now_utc)

    conversation =relationship(
        "Conversation",
        back_populates="documents"
    )