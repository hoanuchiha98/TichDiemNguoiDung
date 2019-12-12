from common.utils.http_status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_201_CREATED, \
    HTTP_202_ACCEPTED
from config import db
from models.point_to_money import PointToMoneyModel, PointToMoneySchema


def get_all(page_number, page_size):
    # return http_status, data, total
    try:
        schema = PointToMoneySchema()
        total = PointToMoneyModel.query.count()
        if total == 0:
            return HTTP_404_NOT_FOUND, None, 0
        items = PointToMoneyModel.query.paginate(page_number, page_size).items
        if items in [None, {}]:
            return HTTP_404_NOT_FOUND, None, 0
        # dump data
        result = schema.dump(items, many=True)
        return HTTP_200_OK, result, total
    except Exception as error:
        print("Error----------------", error)
        return HTTP_400_BAD_REQUEST, None, 0

def get_by_id(point_to_money_id):
    try:
        item = PointToMoneyModel.query.filter_by(id=point_to_money_id).first()
        if item is None:
            return HTTP_404_NOT_FOUND, None
        schema = PointToMoneySchema()
        result = schema.dump(item, many=False)
        return HTTP_200_OK, result
    except Exception as error:
        print("Error------------------", error)
        return HTTP_400_BAD_REQUEST, None

def create(point_to_money_data):
    try:
        schema = PointToMoneySchema()
        new_item = schema.make(point_to_money_data)
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

def update(point_to_money_id, point_to_money_data):
    try:
        schema = PointToMoneySchema()
        item = PointToMoneyModel.query.filter_by(id=point_to_money_id).first()
        print(item)
        if item is None:
            return HTTP_404_NOT_FOUND, None
        new_item = PointToMoneyModel.query.filter_by(id=point_to_money_id).update(point_to_money_data)
        db.session.commit()
        item = PointToMoneyModel.query.filter_by(id=point_to_money_id).first()
        result = schema.dump(item, many=False)
        return HTTP_201_CREATED, result
    except Exception as error:
        print("Error-------------", error)
        db.session.rollback()
        return HTTP_400_BAD_REQUEST, None

def delete(point_to_money_id):
    try:
        item = PointToMoneyModel.query.filter_by(id=point_to_money_id)
        print(item)
        if item is None:
            return HTTP_404_NOT_FOUND
        db.session.delete(item)
        db.session.commit()
        return HTTP_202_ACCEPTED
    except Exception as error:
        print("Error---------------", error)
        return HTTP_400_BAD_REQUEST
