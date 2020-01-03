"""
    Các hàm hỗ trợ gửi response
"""
from flask import jsonify, abort

from common.utils.http_status import ERR_MSG_BAD_REQUEST, HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, \
    SUCCESS_MSG, ERR_MSG_NOT_FOUND, HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN


def send_response(code=400, data=None, total=0, message=""):
    if code == HTTP_200_OK:
        if total==0:
            return jsonify({"code": code, "message": SUCCESS_MSG, "data": data})
        return jsonify({"code": code, "message": SUCCESS_MSG, "data": data, "total": total})
    elif code==HTTP_201_CREATED:
        return jsonify({"code": code, "message": SUCCESS_MSG, "data": data})
    elif code == HTTP_202_ACCEPTED:
        return jsonify({"code": code, "message": SUCCESS_MSG})
    elif code == HTTP_400_BAD_REQUEST:
        return jsonify({"code": code, "message": ERR_MSG_BAD_REQUEST})
    elif code == HTTP_404_NOT_FOUND:
        return jsonify({"code": code, "message": ERR_MSG_NOT_FOUND})
    elif code==HTTP_403_FORBIDDEN:
        return jsonify({"code": code, "message": "Not enough permissions required"})
    else:
        return jsonify({"code": code, "message": message})