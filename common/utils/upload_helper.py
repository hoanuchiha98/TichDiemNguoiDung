import os

from werkzeug.utils import secure_filename

from common.utils.date_helper import current_yyyy_mm_dd
from config import UPLOAD_FOLDER

# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_IMGAGE_EXTENSIONS = ['png', 'jpg', 'jpeg']


def allowed_file_img(filename):
    """
    :param: filename: tên file

    :process:
    - Kiểm tra file hợp lệ trong đuôi ALLOWED_EXTENSIONS
    """
    print(filename)
    if '.' in filename:
        return filename.rsplit('.', 1)[1].lower() in ALLOWED_IMGAGE_EXTENSIONS


def upload_file_img(file=None, type_name=None) -> str:
    """
    Upload file ảnh

    Process:
        - Kiểm tra đuôi ảnh
        - Thêm ảnh


    :param: file: định dạng file có mở rộng là ['png', 'jpg', 'jpeg']
    :return:
        - path - đường dẫn của ảnh
        - None nếu không thêm thành công
    """
    # Validate input
    if file is None:
        return None
    if not allowed_file_img(file.filename):
        return None

    # Check path is not exist then create new folder
    path = UPLOAD_FOLDER + "/"
    if not os.path.exists(path):
        print("make directory")
        os.makedirs(path)
    # file name: 20-11-2019_filename.png
    filename = secure_filename(current_yyyy_mm_dd() + "_" + file.filename)  # file name

    try:
        path = os.path.join(path, filename)
        print('path: ', path)
        file.save(path)
        return path
    except IOError as error:
        print("Cannot save file", error)
        return None
