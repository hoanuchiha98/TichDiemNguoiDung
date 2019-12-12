from common.utils.decode_utils import lazy_hashing
from common.utils.http_status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_201_CREATED, \
    HTTP_202_ACCEPTED
from config import db
from models.user import UserModel, UserSchema


def get_all(page_number, page_size):
    # return http_status, data, total
    try:
        schema = UserSchema()
        total = UserModel.query.count()
        if total == 0:
            return HTTP_404_NOT_FOUND, None, 0
        items = UserModel.query.paginate(page_number, page_size).items
        if items in [None, {}]:
            return HTTP_404_NOT_FOUND, None, 0
        # dump data
        result = schema.dump(items, many=True)
        return HTTP_200_OK, result, total
    except Exception as error:
        print("Error----------------", error)
        return HTTP_400_BAD_REQUEST, None, 0

def get_by_id(user_id):
    try:
        item = UserModel.query.filter_by(id=user_id).first()
        if item is None:
            return HTTP_404_NOT_FOUND, None
        schema = UserSchema()
        result = schema.dump(item, many=False)
        return HTTP_200_OK, result
    except Exception as error:
        print("Error------------------", error)
        return HTTP_400_BAD_REQUEST, None

def create(user_data):
    try:
        schema = UserSchema()
        new_item = schema.make(user_data)
        new_item.password = lazy_hashing(user_data['password'])
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

def update(user_id, user_data):
    try:
        schema = UserSchema()
        item = UserModel.query.filter_by(id=user_id).first()
        print(item)
        if item is None:
            return HTTP_404_NOT_FOUND, None
        new_item = UserModel.query.filter_by(id=user_id).update(user_data)
        db.session.commit()
        item = UserModel.query.filter_by(id=user_id).first()
        result = schema.dump(item, many=False)
        return HTTP_201_CREATED, result
    except Exception as error:
        print("Error-------------", error)
        db.session.rollback()
        return HTTP_400_BAD_REQUEST, None

def delete(user_id):
    try:
        item = UserModel.query.filter_by(id=user_id).first()
        print(item)
        if item is None:
            return HTTP_404_NOT_FOUND
        item.status = 0
        db.session.commit()
        return HTTP_202_ACCEPTED
    except Exception as error:
        print("Error---------------", error)
        return HTTP_400_BAD_REQUEST

def register(user_data):
    try:
        schema = UserSchema()
        new_item = schema.make(user_data)
        new_item.password = lazy_hashing(user_data['password'])
        new_item.role = 1
        new_item.danger = False
        new_item.point = 0
        new_item.status = 1
        new_item.member_id = 0
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

