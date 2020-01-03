from flask import request, abort

from common.utils.http_status import HTTP_401_UNAUTHORIZED
from controllers.auth import decode_token


def get_user_info_from_token():
    """[Lấy thông tin người dùng từ token]
        RETURN: { 'iss': 'com.zalando.connexion',
            'iat': 1568622689,
            'exp': 1568623289,
            'user_id': 32,
            'username': 'string',
            'role': 0,
            'fullname': 'string'
        }
    """
    # token = request.headers['Authorization']
    # if token is None:
    #     return abort(status=HTTP_401_UNAUTHORIZED)
    # user = decode_token(token, None)
    # print("Current user login", user)
    return True

def check_role_user(require_role: int):
    # user_info = get_user_info_from_token()
    # user_role = user_info["role"]
    # user_id = user_info["user_id"]
    # if user_role <= require_role:
    #     return True
    # return False
    return True