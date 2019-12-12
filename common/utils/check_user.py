from models.user import UserModel

def isUserExisted(user_id=-1, user_name="-1"):
    """[kiểm tra xem user có tồn tại không]

    Arguments: 1 trong 2 tham số đều được
        user_id {[int]} -- [user id]
        user_name {[string]} -- [tên user]

    Returns:
        [Bool] -- [True if exist - False if not exist]
    """
    # Check by id
    list_user_by_id = UserModel.query.filter_by(id=user_id).first()
    # Check by name
    list_user_by_name = UserModel.query.filter_by(username=user_name).first()
    if list_user_by_id is not None:
        return True
    if list_user_by_name is not None:
        return True
    return False