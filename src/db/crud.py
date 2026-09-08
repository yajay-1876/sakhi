#----------helper functions---------------#
from datetime import datetime, timezone
def now_utc():
    return datetime.now(tz=timezone.utc)

import uuid
def create_id():
    return str(uuid.uuid4())

#---------------imports------------------#
from typing import Optional, Dict, Any, List
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError

from src.db.database import SessionLocal
from src.db.models import User, Conversation, Message, Document

#---------------core database services------------#

def create_or_get_userid(username: str)->str|None:
    with SessionLocal() as db:
        existing_user=db.query(User).filter(User.username == username).first()
        if existing_user:
            return existing_user.id
        else:
            user_id = create_id()
            user_obj=User(
                id=user_id,
                username=username,
                created_at= now_utc()
            )
            db.add(user_obj)
            db.commit()
            return user_id

def create_new_conversation(user_id: str, title: Optional[str]=None ) -> str:
    ts=now_utc()
    conv_id=create_id()
    with SessionLocal() as db:

       conversation_obj= Conversation(
           id              = conv_id,
           user_id         = user_id,
           title           = title or "Untitled Conversation",
           last_interacted = ts
       )
       db.add(conversation_obj)
       db.commit()
    return conv_id


def get_chat_history_by_conv_id(conv_id: str) -> Optional[List[Dict]]:
    with SessionLocal() as db:
        conv = db.get(Conversation, conv_id)
        if conv is None:
            return None
        return [{"role": m.role, "content": m.content} for m in conv.messages]

def get_conversations_by_user(user_id:str) -> Dict[str, str]:
    with SessionLocal() as db:
        user_obj=db.get(User, user_id)
        if not user_obj:
            return {}
        return {row.id: row.title for row in user_obj.conversations}

def add_message(conv_id: str, role: str, content: str):
    with SessionLocal() as db:
        ts=now_utc()
        conv_obj= db.get(Conversation, conv_id)         # ORM way of searching row .get(Table, primary key)
        if conv_obj is None:
            return False
        message_obj= Message(
               conversation_id = conv_id,
               role            = role,
               content         = content,
               ts              = ts
           )
        db.add(message_obj)
        conv_obj.last_interacted=ts
        db.commit()


def add_document(doc_id:str, conv_id: str, filename: str)->bool:
    with SessionLocal() as db:
        exists = (
            db.query(Document)
                .filter(Document.document_id==doc_id, Document.conversation_id==conv_id)
                .first()
            is not None
        )
        if exists:
            return False
        else:
            doc_obj= Document(
                id              = create_id(),
                document_id     = doc_id,
                conversation_id = conv_id,
                filename        = filename,
                uploaded_at     = now_utc()
            )
            db.add(doc_obj)
            db.commit()
            return True


def get_documents(conv_id:str)->list:
    with SessionLocal() as db:
        conv_obj=db.get(Conversation, conv_id)
        if not conv_obj:
            return []
        documents= conv_obj.documents
        return [doc.id for doc in documents]

