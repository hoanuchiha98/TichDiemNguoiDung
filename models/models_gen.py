# coding: utf-8
from sqlalchemy import Boolean, Column, Date, Float, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Bill(Base):
    __tablename__ = 'bill'

    id = Column(Integer, primary_key=True, server_default=text("nextval('bill_id_seq'::regclass)"))
    user_id = Column(Integer)
    money_bill = Column(Float(53))
    date_created = Column(Date)
    conversion_point = Column(Integer)
    conversion_point_last = Column(Integer)
    ship_money = Column(Float(53))


class BillDetail(Base):
    __tablename__ = 'bill_detail'

    id = Column(Integer, primary_key=True, server_default=text("nextval('bill_detail_id_seq'::regclass)"))
    bill_id = Column(Integer)
    product_id = Column(Integer)
    count = Column(Integer)


class MoneyToPoint(Base):
    __tablename__ = 'money_to_point'

    id = Column(Integer, primary_key=True, server_default=text("nextval('money_to_point_id_seq'::regclass)"))
    start_date = Column(Date)
    end_date = Column(Date)
    rate_to_point = Column(Float(53))


class PointToMoney(Base):
    __tablename__ = 'point_to_money'

    id = Column(Integer, primary_key=True, server_default=text("nextval('point_to_money_id_seq'::regclass)"))
    start_date = Column(Date)
    end_date = Column(Date)
    rate_to_money = Column(Float(53))


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, server_default=text("nextval('product_id_seq'::regclass)"))
    product_name = Column(String)
    product_price = Column(Float(53))


class TypeMember(Base):
    __tablename__ = 'type_member'

    id = Column(Integer, primary_key=True, server_default=text("nextval('type_member_id_seq'::regclass)"))
    name_member = Column(String)
    price = Column(Integer)
    date_created = Column(Date)
    status = Column(Integer)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, server_default=text("nextval('user_id_seq'::regclass)"))
    username = Column(String)
    password = Column(String)
    fullname = Column(String)
    role = Column(Integer)
    danger = Column(Boolean)
    dob = Column(Date)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String)
    point = Column(Integer)
    status = Column(Integer)
    member_id = Column(Integer)
