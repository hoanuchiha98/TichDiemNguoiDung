from flask import Response

from common.utils.check_role import check_role_user
from common.utils.http_status import HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
from common.utils.response_status_utils import send_response
from services import bill_service

def get_all(page_number=1, page_size=20):
    role = check_role_user(0)
    if role==False:
        send_response(code=HTTP_404_NOT_FOUND)
    result = bill_service.get_all(page_number=page_number, page_size=page_size)
    data = result[1]
    http_status = result[0]
    # return
    return send_response(code=http_status, data=data)

def create(bill_data):
    role = check_role_user(0)
    if role==False:
        return send_response(code=HTTP_404_NOT_FOUND)
    result = bill_service.create(bill_data=bill_data)
    http_status = result[0]
    data = result[1]
    # return
    return send_response(code=http_status, data=data)

def get_by_id(bill_id):
    result = bill_service.get_by_id(bill_id=bill_id)
    http_status = result[0]
    data = result[1]
    # return
    return send_response(code=http_status, data=data)

def update(bill_id, bill_data):
    role = check_role_user(1)
    if role == False:
        return send_response(code=HTTP_404_NOT_FOUND)
    result = bill_service.update(bill_id=bill_id, bill_data=bill_data)
    http_status = result[0]
    data = result[1]
    # return
    return send_response(code=http_status, data=data)

def delete(bill_id):
    role = check_role_user(0)
    if role == False:
        send_response(code=HTTP_404_NOT_FOUND)
    result = bill_service.delete(bill_id=bill_id)
    # return
    return send_response(code=result)

