import base64
import os

from common.utils.check_role import get_user_info_from_token
from common.utils.response_status_utils import send_response
from flask import Response
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
from common.utils import upload_helper

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']

def allowed_file(filename):
    """
    Kiểm tra file hợp lệ trong đuôi ALLOWED_EXTENSIONS
    """
    print(filename)
    if '.' in filename:
        return filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def mapping_type(type_name=None):
    """
    Ánh xạ lại type
    :param type_name: ['baskets', 'monitors_objects', 'social_objects', 'users']
    :return:
    """
    types = {}
    for i, value in enumerate(FOLDER_NAMES):
        types[str(i)] = value
    print(types)
    return types.get(type_name)

def upload_file(type_name=None, file=None):
    user_info = get_user_info_from_token()
    username = user_info.get("username")

    path = ""
    if username is not None:
        path = upload_helper.upload_file_img(file=file, type_name=type_name, username=username)
        print("Path--------", path)
    if path in (None, ""):
        return send_response(message="Cannot upload file", code=400)
    return send_response(message="Upload success", data={"path": path}, code=200)


def get_image_base_64(relative_path):
    """
        API: GET /image
    """
    user_info = get_user_info_from_token()
    if user_info is None:
        print('user not authentiaction....')
        return HTTP_401_UNAUTHORIZED

    path = ''
    path = os.path.join(path, relative_path)
    print("get image path:", path)

    try:
        with open(path, "rb") as image_file:
            image_binary = base64.b64encode(image_file.read())
            return Response(image_binary, mimetype='text/csv')

    except IOError as error:
        print(error)
        print("Can't not open file")
        return HTTP_404_NOT_FOUND
