from common.utils.http_status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_202_ACCEPTED
from models.product import ProductModel, ProductSchema
from config import db

def get_all(page_number, page_size):
    # return http_status, data, total
    try:
        schema = ProductSchema()
        total = ProductModel.query.count()
        if total == 0:
            return HTTP_404_NOT_FOUND, None, 0
        items = ProductModel.query.paginate(page_number, page_size).items
        if items in [None, {}]:
            return HTTP_404_NOT_FOUND, None, 0
        # dump data
        result = schema.dump(items, many=True)
        return HTTP_200_OK, result, total
    except Exception as error:
        print("Error----------------", error)
        return HTTP_400_BAD_REQUEST, None, 0

def get_by_id(product_id):
    try:
        item = ProductModel.query.filter_by(id=product_id).first()
        if item is None:
            return HTTP_404_NOT_FOUND, None
        schema = ProductSchema()
        result = schema.dump(item, many=False)
        return HTTP_200_OK, result
    except Exception as error:
        print("Error------------------", error)
        return HTTP_400_BAD_REQUEST, None

def create(product_data):
    try:
        schema = ProductSchema()
        new_item = schema.make(product_data)
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

def update(product_id, product_data):
    try:
        schema = ProductSchema()
        item = ProductModel.query.filter_by(id=product_id).first()
        print(item)
        if item is None:
            return HTTP_404_NOT_FOUND, None
        new_item = ProductModel.query.filter_by(id=product_id).update(product_data)
        db.session.commit()
        item = ProductModel.query.filter_by(id=product_id).first()
        result = schema.dump(item, many=False)
        return HTTP_201_CREATED, result
    except Exception as error:
        print("Error-------------", error)
        db.session.rollback()
        return HTTP_400_BAD_REQUEST, None

def delete(product_id):
    try:
        item = ProductModel.query.filter_by(id=product_id).first()
        print(item)
        if item is None:
            return HTTP_404_NOT_FOUND
        db.session.delete(item)
        db.session.commit()
        return HTTP_202_ACCEPTED
    except Exception as error:
        print("Error---------------", error)
        return HTTP_400_BAD_REQUEST