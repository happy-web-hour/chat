import uuid
from datetime import datetime

from src.repository.ChatRepository import ChatRepository


class ChatService:
    def __init__(self, repository: ChatRepository):
        self.__repository = repository

    def post_message(self, room_id: str, user_id: str, message: str):
        message = {
            "messageId": str(uuid.uuid4()),
            "userId": user_id,
            "message": message,
            "timestamp": datetime.timestamp(datetime.now()),
            "systemMessage": False
        }
        return self.__repository.post_message(
            room_id=room_id,
            message=message
        )

    def get_all_messages(self, room_id: str):
        messages = self.__repository.get_all_messages(
            room_id=room_id
        )
        return sorted(messages, key=lambda k: k['timestamp'])

    def get_messages_after(self, room_id: str, message_id: str):
        messages = self.__repository.get_all_messages(
            room_id=room_id
        )
        sorted_messages = sorted(messages, key=lambda k: k['timestamp'])
        i = 0
        for i in range(len(sorted_messages)):
            if sorted_messages[i]["messageId"] == message_id:
                break

        return [sorted_messages[x] for x in range(i, len(sorted_messages))]

    def add_user(self, room_id: str, user_id: str):
        message = {
            "messageId": str(uuid.uuid4()),
            "userId": user_id,
            "message": f"Added user {user_id}",
            "timestamp": datetime.timestamp(datetime.now()),
            "systemMessage": True
        }
        return self.__repository.post_message(
            room_id=room_id,
            message=message
        )

    def delete_user(self, room_id: str, user_id: str):
        message = {
            "messageId": str(uuid.uuid4()),
            "userId": user_id,
            "message": f"Delete user {user_id}",
            "timestamp": datetime.timestamp(datetime.now()),
            "systemMessage": True
        }
        return self.__repository.post_message(
            room_id=room_id,
            message=message
        )

    def delete_chat(self, room_id: str):
        return self.__repository.delete_chat(
            room_id=room_id
        )
