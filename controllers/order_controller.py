from common.utils.http_status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from common.utils.response_status_utils import send_response
from services import order_service


def create_orders(cart_data: dict):
    result = order_service.create_order(order_data=cart_data)
    return send_response(code=HTTP_200_OK) if result==True else send_response(code=HTTP_400_BAD_REQUEST)
