from flask import Blueprint, request
from flask_cors import cross_origin

from src.controller import service
from src.controller.UtilController import UtilController
from src.library.logger.Logger import Logger

chat_controller = Blueprint('ChatController', __name__)


class ChatController:
    @staticmethod
    @cross_origin()
    @chat_controller.route('/chat/<string:room_id>/<string:user_id>', methods=['POST'])
    def post_message(room_id: str, user_id: str):
        response: dict = {}
        status_code: int = 200
        try:
            Logger.info(f"post_chat: room_id={room_id} user_id={user_id}")
            service.post_message(
                room_id=room_id,
                user_id=user_id,
                message=request.json["message"]
            )
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @chat_controller.route('/chat/<string:room_id>', methods=['GET'])
    def get_all_messages(room_id: str):
        response: dict
        status_code: int = 200
        try:
            Logger.info(f"get_all_messages: room_id={room_id}")
            response = service.get_all_messages(
                room_id=room_id
            )
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @chat_controller.route('/chat/<string:room_id>/<string:message_id>', methods=['GET'])
    def get_messages_after(room_id: str, message_id: str):
        response: dict
        status_code: int = 200
        try:
            Logger.info(f"get_messages_after: room_id={room_id} message_id={message_id}")
            response = service.get_messages_after(
                room_id=room_id,
                message_id=message_id
            )
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @chat_controller.route('/chat/<string:room_id>/<string:user_id>', methods=['PATCH'])
    def add_user(room_id: str, user_id: str):
        response: dict = {}
        status_code: int = 200
        try:
            Logger.info(f"add_user: room_id={room_id} user_id={user_id}")
            service.add_user(
                room_id=room_id,
                user_id=user_id
            )
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @chat_controller.route('/chat/<string:room_id>/<string:user_id>', methods=['DELETE'])
    def delete_user(room_id: str, user_id: str):
        response: dict = {}
        status_code: int = 200
        try:
            Logger.info(f"delete_user: room_id={room_id} user_id={user_id}")
            service.delete_user(
                room_id=room_id,
                user_id=user_id
            )
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @chat_controller.route('/chat/<string:room_id>', methods=['DELETE'])
    def delete_chat(room_id: str):
        response: dict = {}
        status_code: int = 200
        try:
            Logger.info(f"delete_chat: room_id={room_id}")
            service.delete_chat(
                room_id=room_id
            )
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @chat_controller.route('/chat/<string:room_id>', methods=['POST'])
    def create_chat(room_id: str):
        response: dict = {}
        status_code: int = 200
        try:
            Logger.info(f"create_chat: room_id={room_id}")
            service.create_chat(
                room_id=room_id
            )
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)
