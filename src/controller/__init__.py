from src.repository.ChatRepository import ChatRepository
from src.service.ChatService import ChatService

repository = ChatRepository()

service = ChatService(
    repository=repository
)
