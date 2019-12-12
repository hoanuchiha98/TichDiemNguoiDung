from common.utils.http_status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_202_ACCEPTED
from models.type_member import TypeMemberModel, TypeMemberSchema
from config import db
from datetime import datetime

def get_all(page_number, page_size):
    # return http_status, data, total
    try:
        schema = TypeMemberSchema()
        total = TypeMemberModel.query.count()
        if total == 0:
            return HTTP_404_NOT_FOUND, None, 0
        items = TypeMemberModel.query.paginate(page_number, page_size).items
        if items in [None, {}]:
            return HTTP_404_NOT_FOUND, None, 0
        # dump data
        result = schema.dump(items, many=True)
        return HTTP_200_OK, result, total
    except Exception as error:
        print("Error----------------", error)
        return HTTP_400_BAD_REQUEST, None, 0

def get_by_id(type_member_id):
    try:
        item = TypeMemberModel.query.filter_by(id=type_member_id).first()
        if item is None:
            return HTTP_404_NOT_FOUND, None
        schema = TypeMemberSchema()
        result = schema.dump(item, many=False)
        return HTTP_200_OK, result
    except Exception as error:
        print("Error------------------", error)
        return HTTP_400_BAD_REQUEST, None

def create(type_member_data):
    try:
        schema = TypeMemberSchema()
        new_item = schema.make(type_member_data)
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

def update(type_member_id, type_member_data):
    try:
        schema = TypeMemberSchema()
        item = TypeMemberModel.query.filter_by(id=type_member_id).first()
        print(item)
        if item is None:
            return HTTP_404_NOT_FOUND, None
        if type_member_data('date_created') is not None:
            type_member_data.pop('date_created')
        new_item = TypeMemberModel.query.filter_by(id=type_member_id).update(type_member_data)
        db.session.commit()
        item = TypeMemberModel.query.filter_by(id=type_member_id).first()
        result = schema.dump(item, many=False)
        return HTTP_201_CREATED, result
    except Exception as error:
        print("Error-------------", error)
        db.session.rollback()
        return HTTP_400_BAD_REQUEST, None

def delete(type_member_id):
    try:
        item = TypeMemberModel.query.filter_by(id=type_member_id).first()
        print(item)
        if item is None:
            return HTTP_404_NOT_FOUND
        db.session.delete(item)
        db.session.commit()
        return HTTP_202_ACCEPTED
    except Exception as error:
        print("Error---------------", error)
        return HTTP_400_BAD_REQUEST