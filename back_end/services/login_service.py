import re
from headers import *
from services.mysql_service import db


def checkLoginInfo(user_info):
    # 检查用户输入的用户名是否存在
    if not db.checkUserNameExistence(user_info['user_name']):
        return USER_NOT_EXIST, None

    # 检查用户输入的密码是否正确
    user_tuple = db.getUser("user_name", user_info['user_name'])
    user = db.tupleToDict(user_tuple, USER_KEY)
    if user_info['password'] != user['password']:
        return WRONG_PASSWORD, None

    return LOGIN_SUCCESS, user

