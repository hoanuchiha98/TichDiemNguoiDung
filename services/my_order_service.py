from sqlalchemy import func

from common.database.database_helper import execute_select_query
from common.utils.http_status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from config import db
from models.bill import BillSchema, BillModel
from models.bill_detail import BillDetailSchemaDTO, BillDetailModel
from models.product import ProductModel


def customer_order(user_id, desc_date: bool=True):
    try:
        schema = BillSchema()

        order = BillModel.query.filter_by(user_id=user_id).order_by\
            (BillModel.date_created.desc()).all() if desc_date==True else \
            BillModel.query.filter_by(user_id=user_id).order_by \
                (BillModel.date_created.asc()).all()
        result = schema.dump(order, many=True)
        return result, HTTP_200_OK
    except Exception as error:
        return None, HTTP_400_BAD_REQUEST

def custom_order_detail(bill_id: int):
    try:
        # print("skdj nfd dgd igjdi ")
        # bill_detail = db.session.query(BillDetailModel.id.label('bill_detail_id'),\
        #                                BillModel.id.label('bill_id'),\
        #                                ProductModel.id.label('product_id'),
        #                                ProductModel.product_name.label('product_name'),\
        #                                ProductModel.description.label('product_description'),\
        #                                ProductModel.photo.label('photo'),
        #                                BillDetailModel.count.label('count'),
        #                 func(BillDetailModel.count * ProductModel.product_price).label("into_money")).\
        # filter(ProductModel.id==BillDetailModel.product_id).\
        # filter(BillDetailModel.bill_id == BillModel.id).\
        # filter(BillModel.id==bill_id).order_by(func(BillDetailModel.count * ProductModel.product_price).desc())\
        # .all()
        # print("Bill Detail::UserId=========", bill_detail)
        # result = schema.dump(bill_detail, many=True)
        select_query = f"""
                    select bd.id as bill_detail_id,
                           p.id as product_id,
                           b.id as bill_id,
                           p.product_name as product_name,
                           p.photo as photo,
                           bd.count as count_detail,
                           p.description as product_description,
                           p.product_price * bd.count as into_money
                    from bill b, bill_detail bd, product p
                    where b.id=bd.bill_id and p.id=bd.product_id
                    and b.id = {bill_id}
        """
        print("Sql Query::===", select_query)
        result = execute_select_query(select_query)
        print(result)
        return result, HTTP_200_OK
    except Exception as error:
        return None, HTTP_400_BAD_REQUEST