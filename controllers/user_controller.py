from common.utils.check_role import check_role_user
from common.utils.check_user import isUserExisted
from common.utils.http_status import HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
from common.utils.response_status_utils import send_response
from services import user_service

def get_all(page_number=1, page_size=20):
    role = check_role_user(0)
    if role==False:
        send_response(code=HTTP_404_NOT_FOUND)
    result = user_service.get_all(page_number=page_number, page_size=page_size)
    http_status = result[0]
    data = result[1]
    total = result[2]
    # return
    return send_response(code=http_status, data=data, total=total)

def create(user_data):
    role = check_role_user(0)
    if role==False:
        return send_response(code=HTTP_404_NOT_FOUND)
    if isUserExisted(user_name = user_data["username"])==True:
        return send_response(code=HTTP_409_CONFLICT, message="Username already exists when registering new account")
    result = user_service.create(user_data=user_data)
    http_status = result[0]
    data = result[1]
    # return
    return send_response(code=http_status, data=data)

def get_by_id(user_id):
    result = user_service.get_by_id(user_id=user_id)
    http_status = result[0]
    data = result[1]
    # return
    return send_response(code=http_status, data=data)

def update(user_id, user_data):
    role = check_role_user(1)
    if role == False:
        return send_response(code=HTTP_404_NOT_FOUND)
    result = user_service.update(user_id=user_id, user_data=user_data)
    http_status = result[0]
    data = result[1]
    # return
    return send_response(code=http_status, data=data)

def delete(user_id):
    role = check_role_user(0)
    if role == False:
        send_response(code=HTTP_404_NOT_FOUND)
    result = user_service.delete(user_id=user_id)
    # return
    return send_response(code=result)

def register(user_data):
    if isUserExisted(user_name = user_data["username"])==True:
        return send_response(code=HTTP_409_CONFLICT, message="Username already exists when registering new account")
    result = user_service.register(user_data=user_data)
    http_status = result[0]
    data = result[1]
    # return
    return send_response(code=http_status, data=data)

if __name__ == '__main__':
    print((1, 2, None))
