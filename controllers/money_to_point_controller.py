from common.utils.check_role import check_role_user
from common.utils.http_status import HTTP_404_NOT_FOUND
from common.utils.response_status_utils import send_response
from services import money_to_point_service

def get_all(page_number=1, page_size=20):
    role = check_role_user(0)
    if role==False:
        send_response(code=HTTP_404_NOT_FOUND)
    result = money_to_point_service.get_all(page_number=page_number, page_size=page_size)
    http_status = result[0]
    data = result[1]
    total = result[2]
    # return
    return send_response(code=http_status, data=data, total=total)

def create(money_to_point_data):
    role = check_role_user(0)
    if role==False:
        return send_response(code=HTTP_404_NOT_FOUND)
    result = money_to_point_service.create(money_to_point_data=money_to_point_data)
    http_status = result[0]
    data = result[1]
    # return
    return send_response(code=http_status, data=data)

def get_by_id(money_to_point_id):
    result = money_to_point_service.get_by_id(money_to_point_id=money_to_point_id)
    http_status = result[0]
    data = result[1]
    # return
    return send_response(code=http_status, data=data)

def update(money_to_point_id, money_to_point_data):
    role = check_role_user(1)
    if role == False:
        return send_response(code=HTTP_404_NOT_FOUND)
    result = money_to_point_service.update(money_to_point_id=money_to_point_id, money_to_point_data=money_to_point_data)
    http_status = result[0]
    data = result[1]
    # return
    return send_response(code=http_status, data=data)

def delete(money_to_point_id):
    role = check_role_user(0)
    if role == False:
        send_response(code=HTTP_404_NOT_FOUND)
    result = money_to_point_service.delete(money_to_point_id=money_to_point_id)
    # return
    return send_response(code=result)

