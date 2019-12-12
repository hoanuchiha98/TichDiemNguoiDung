from common.utils.http_status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_202_ACCEPTED
from models.bill import BillModel, BillSchema
from config import db
from datetime import datetime

def get_all(page_number, page_size):
    # return http_status, data, total
    try:
        schema = BillSchema()
        total = BillModel.query.count()
        if total == 0:
            return HTTP_404_NOT_FOUND, None, 0
        items = BillModel.query.paginate(page_number, page_size).items
        if items in [None, {}]:
            return HTTP_404_NOT_FOUND, None, 0
        # dump data
        result = schema.dump(items, many=True)
        return HTTP_200_OK, result, total
    except Exception as error:
        print("Error----------------", error)
        return HTTP_400_BAD_REQUEST, None, 0

def get_by_id(bill_id):
    try:
        item = BillModel.query.filter_by(id=bill_id).first()
        if item is None:
            return HTTP_404_NOT_FOUND, None
        schema = BillSchema()
        result = schema.dump(item, many=False)
        return HTTP_200_OK, result
    except Exception as error:
        print("Error------------------", error)
        return HTTP_400_BAD_REQUEST, None

def create(bill_data):
    try:
        schema = BillSchema()
        new_item = schema.make(bill_data)
        new_item.date_created = datetime.now()
        db.session.add(new_item)
        # commit
        db.session.commit()
        # dump data
        result = schema.dump(new_item, many=False)
        print("items-------------", result)
        return HTTP_201_CREATED, result
    except Exception as error:
        print("Error----------------", error)
        db.session.rollback()
        return HTTP_400_BAD_REQUEST, None

def update(bill_id, bill_data):
    try:
        schema = BillSchema()
        item = BillModel.query.filter_by(id=bill_id).first()
        print(item)
        if item is None:
            return HTTP_404_NOT_FOUND, None
        if bill_data('date_created') is not None:
            bill_data.pop('date_created')
        new_item = BillModel.query.filter_by(id=bill_id).update(bill_data)
        db.session.commit()
        item = BillModel.query.filter_by(id=bill_id).first()
        result = schema.dump(item, many=False)
        return HTTP_201_CREATED, result
    except Exception as error:
        print("Error-------------", error)
        db.session.rollback()
        return HTTP_400_BAD_REQUEST, None

def delete(bill_id):
    try:
        item = BillModel.query.filter_by(id=bill_id).first()
        print(item)
        if item is None:
            return HTTP_404_NOT_FOUND
        db.session.delete(item)
        db.session.commit()
        return HTTP_202_ACCEPTED
    except Exception as error:
        print("Error---------------", error)
        return HTTP_400_BAD_REQUEST