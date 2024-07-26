from http import HTTPStatus
from flask import jsonify
from helpers.errcode import ErrCode


class HTTPHelper:
    @staticmethod
    def generate_response(code=0, msg='', data=None, token=None):
        response = {
            'code': code,
            'msg': ErrCode.get_error_message(code),
            'data': data if data is not None else {},
            "token": token,
        }

        if msg != "":
            response['msg'] += (',' + msg)

        return jsonify(response), HTTPStatus.OK
