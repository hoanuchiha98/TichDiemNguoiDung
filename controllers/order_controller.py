from common.utils.http_status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from common.utils.response_status_utils import send_response
from services import order_service, my_order_service


def create_orders(cart_data: dict):
    result = order_service.create_order(order_data=cart_data)
    return send_response(code=HTTP_200_OK) if result==True else send_response(code=HTTP_400_BAD_REQUEST, message=result[1])

def customer_order(user_id: int, desc_date: bool=True):
    result = my_order_service.customer_order(user_id=user_id, desc_date=desc_date)
    http_status = result[1]
    data = result[0]
    # return
    return send_response(code=http_status, data=data)

def custom_order_detail(bill_id: int):
    print("bchsbfhjsdhjshd")
    result = my_order_service.custom_order_detail(bill_id=bill_id)
    http_status = result[1]
    data = result[0]
    # return
    return send_response(code=http_status, data=data)