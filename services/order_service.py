from config import db
from models.bill import BillSchema
from datetime import datetime

from models.bill_detail import BillDetailSchema


def create_order(order_data: dict):
    try:
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
        # commit
        db.session.commit()
        return True
    except Exception as erroe:
        db.session.rollback()
        return False
