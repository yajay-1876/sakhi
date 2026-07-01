from src.backend.api.login_api import router as login_router
from src.backend.api.conversations_api import router as conversations_router
from src.backend.api.chat_api import router as chat_router
from src.backend.api.document_api import router as document_router
routers=[
    login_router,
    conversations_router,
    chat_router,
    document_router
]



# from .users import router as users_router
# from .conversations import router as conversations_router
# from .messages import router as messages_router
# from .documents import router as documents_router
# from .rag import router as rag_router
#
# routers = [
#     users_router,
#     conversations_router,
#     messages_router,
#     documents_router,
#     rag_router,
# ]