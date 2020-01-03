from common.utils.response_status_utils import send_response
from services import accumulate_points_member_service


def accumulate_points(user_id: int, bill_money: int):
    result = accumulate_points_member_service.accumulate_points(user_id=user_id, bill_money=bill_money)
    http_status = result[1]
    data = result[0]
    # return
    return send_response(code=http_status, data=data)

def extract_type_member(user_id: int):
    result = accumulate_points_member_service.extract_type_member(user_id=user_id)
    http_status = result[0]
    data = result[1]
    print(data)
    # return
    return send_response(code=http_status, data=data)

def use_point_pay(user_id: int, bill_money: int):
    result = accumulate_points_member_service.use_point_pay(user_id=user_id, bill_money=bill_money)
    http_status = result[0]
    data = result[1]
    print(data)
    # return
    return send_response(code=http_status, data=data)