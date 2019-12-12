from common.utils.http_status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_201_CREATED, \
    HTTP_202_ACCEPTED
from config import db
from models.money_to_point import MoneyToPointModel, MoneyToPointSchema


def get_all(page_number, page_size):
    # return http_status, data, total
    try:
        schema = MoneyToPointSchema()
        total = MoneyToPointModel.query.count()
        if total == 0:
            return HTTP_404_NOT_FOUND, None, 0
        items = MoneyToPointModel.query.paginate(page_number, page_size).items
        if items in [None, {}]:
            return HTTP_404_NOT_FOUND, None, 0
        # dump data
        result = schema.dump(items, many=True)
        return HTTP_200_OK, result, total
    except Exception as error:
        print("Error----------------", error)
        return HTTP_400_BAD_REQUEST, None, 0

def get_by_id(money_to_point_id):
    try:
        item = MoneyToPointModel.query.filter_by(id=money_to_point_id).first()
        if item is None:
            return HTTP_404_NOT_FOUND, None
        schema = MoneyToPointSchema()
        result = schema.dump(item, many=False)
        return HTTP_200_OK, result
    except Exception as error:
        print("Error------------------", error)
        return HTTP_400_BAD_REQUEST, None

def create(money_to_point_data):
    try:
        schema = MoneyToPointSchema()
        new_item = schema.make(money_to_point_data)
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

def update(money_to_point_id, money_to_point_data):
    try:
        schema = MoneyToPointSchema()
        item = MoneyToPointModel.query.filter_by(id=money_to_point_id).first()
        print(item)
        if item is None:
            return HTTP_404_NOT_FOUND, None
        new_item = MoneyToPointModel.query.filter_by(id=money_to_point_id).update(money_to_point_data)
        db.session.commit()
        item = MoneyToPointModel.query.filter_by(id=money_to_point_id).first()
        result = schema.dump(item, many=False)
        return HTTP_201_CREATED, result
    except Exception as error:
        print("Error-------------", error)
        db.session.rollback()
        return HTTP_400_BAD_REQUEST, None

def delete(money_to_point_id):
    try:
        item = MoneyToPointModel.query.filter_by(id=money_to_point_id)
        print(item)
        if item is None:
            return HTTP_404_NOT_FOUND
        db.session.delete(item)
        db.session.commit()
        return HTTP_202_ACCEPTED
    except Exception as error:
        print("Error---------------", error)
        return HTTP_400_BAD_REQUEST
