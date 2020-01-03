from config import db
from models.bill import BillSchema
from datetime import datetime

from models.bill_detail import BillDetailSchema
from models.product import ProductModel
from models.user import UserModel


def create_order(order_data: dict):
    try:
        message=[]
        schema = BillSchema()
        bill_data = {
            "user_id": order_data["user_id"],
            "money_bill": order_data["money_bill"],
            "date_created": datetime.now(),
            "conversion_point": order_data["conversion_point"]
        }
        bill = schema.make(bill_data)
        db.session.add(bill)
        db.session.flush()
        db.session.refresh(bill)
        bill_detail_schema = BillDetailSchema()
        for item in order_data["cart"]:
            bill_detail_data = {
                "bill_id": bill.id,
                "product_id": item["id"],
                "count": item["quantity"]
            }
            bill_detail = bill_detail_schema.make(bill_detail_data)
            db.session.add(bill_detail)
            db.session.flush()
            db.session.refresh(bill_detail)
            product_stock = ProductModel.query.filter_by(id=item["id"]).first()
            if product_stock.count > item["quantity"]:
                count = product_stock.count - item["quantity"]
                db.session.query(ProductModel).filter_by(id=item["id"]).update({'count':count})
                db.session.flush()
            else:
                message.append(f"""{product_stock.product_name} trong kho chỉ có {item["quantity"]} không đủ cung cấp""")
        if len(message)!=0:
            message_str = ",".join(message)
            return False, message_str
        # cập nhật điểm
        user = UserModel.query.filter_by(id=order_data["user_id"]).first();
        if user is None:
            return False, "Không tìm thấy người dùng"
        user_point = int(user.point)
        # Cập nhật điểm
        user_point += int((order_data["money_bill"]) / 100)
        user.point = user_point
        db.session.add(user)
        db.session.flush()
        db.session.refresh(user)
        # commit
        db.session.commit()
        return True
    except Exception as erroe:
        db.session.rollback()
        return False, "Lỗi server"
