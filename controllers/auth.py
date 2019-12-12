import time
import six
from flask import Response
from jose import jwt, JWTError
from werkzeug.exceptions import Unauthorized
from common.utils.decode_utils import lazy_hashing
from models.user import UserModel

JWT_ISSUER = 'com.zalando.connexion'
JWT_SECRET = 'nWSEuoWcbeKSN'
JWT_LIFETIME_SECONDS = 60*60*24*30  # Time life of session
JWT_ALGORITHM = 'HS256'

def generate_token(auth_payload, admin=False):
    """
        API: POST /authenticate
    """
    username = auth_payload['username']
    password = auth_payload['password']

    if admin == False:
        user = UserModel.query.filter_by(
            username=username,
            password=lazy_hashing(password), status=1).first()
    else:
        user = UserModel.query.filter_by(
            username=username,
            password=lazy_hashing(password),
            role=0, status=1).first()

    if user is not None:
        timestamp = _current_timestamp()
        payload = {
            "iss": JWT_ISSUER,
            "iat": int(timestamp),
            "exp": int(timestamp + JWT_LIFETIME_SECONDS),
            "user_id": user.id,
            "username": user.username,
            "role": user.role,
            "fullname": user.fullname
        }
        # return { "token": jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM) }
        return {"token": jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM), "fullname": user.fullname}
    else:
        return Response('The username or password is invaild!', status=400)


def decode_token(token, required_scopes):
    try:
        print("Decode--------", )
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        six.raise_from(Unauthorized, e)

def decode_admin_token(token, required_scopes):
    try:
        result = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        role = result.get('role')
        if role==0:
            return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        six.raise_from(Unauthorized, e)


def _current_timestamp() -> int:
    return int(time.time())