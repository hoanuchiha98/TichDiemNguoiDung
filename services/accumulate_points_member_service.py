from common.utils.http_status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from config import db
from models.type_member import TypeMemberModel
from models.user import UserModel, UserSchema

def accumulate_points(user_id: int, bill_money: int):
    try:
        user = UserModel.query.filter_by(id=user_id).first();
        if user is None:
            return HTTP_400_BAD_REQUEST, None
        user_point = int(user.point)
        # Cập nhật điểm
        user_point += int((bill_money)/100)
        user.point = user_point
        db.session.add(user)
        db.session.flush()
        db.session.refresh(user)
        db.session.commit()
        # dump
        result = UserSchema().dump(user, many=False)
        return HTTP_200_OK, result
    except Exception as error:
        db.session.rollback()
        return HTTP_400_BAD_REQUEST, None

def use_point_pay(user_id: int, bill_money: int):
    try:
        user = UserModel.query.filter_by(id=user_id).first();
        if user is None:
            return HTTP_400_BAD_REQUEST, None
        point = int(user.point)
        if point < bill_money:
            bill_money = bill_money - point
            point = 0
        else:
            bill_money = 0
            point = point - bill_money
        # dump data
        data = {
            'bill_money': bill_money,
            'point': point
        }
        print("Data============", data)
        return HTTP_200_OK, data
    except Exception as error:
        return HTTP_400_BAD_REQUEST, None

def extract_type_member(user_id: int):
    try:
        user = UserModel.query.filter_by(id=user_id).first();
        if user is None:
            return HTTP_400_BAD_REQUEST, None
        point = int(user.point)
        type_member = TypeMemberModel.query.order_by(TypeMemberModel.price).all()
        print("Type member=================", type_member)
        name_member = ""
        for type in type_member:
            if point >= type.price:
                name_member = type.name_member
                break
            break
        print("Type member=================", name_member)
        return HTTP_200_OK, {"point": point, "type_member": name_member}
    except Exception as e:
        print("Error::===========", str(e))
        return HTTP_400_BAD_REQUEST, None