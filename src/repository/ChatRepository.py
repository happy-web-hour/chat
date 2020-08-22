import os

from src.library.database.Mongo import Mongo


class ChatRepository:
    def __init__(self):
        self.__mongo: Mongo = Mongo(
            host=os.getenv("MONGO_HOST"),
            port=int(os.getenv("MONGO_PORT")),
            default_db=os.getenv("MONGO_INITDB_DATABASE")
        )
        self.__chat = os.getenv("MONGO_CHAT_DB")

    def post_message(self, room_id: str, message: dict):
        self.__mongo.push_element(
            collection=self.__chat,
            query={
                "roomId": room_id
            },
            obj={
                "messages": message
            }
        )

    def get_all_messages(self, room_id: str):
        arr =  self.__mongo.find_by(
            collection=self.__chat,
            query={
                "roomId": room_id
            }
        )
        return arr["messages"]

    def delete_chat(self, room_id: str):
        self.__mongo.delete_one(
            collection=self.__chat,
            query={
                "roomId": room_id
            }
        )

    def create_chat(self, chat: dict):
        self.__mongo.insert_one(
            collection=self.__chat,
            elem=chat
        )
