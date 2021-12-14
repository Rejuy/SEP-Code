import re
from headers import *
from services.mysql_service import db
from services.code_service import coder
from datetime import datetime


admin_secret_code = ""


def checkLoginInfo(user_info):
    # 检查用户输入的用户名是否存在
    if not db.checkUserNameExistence(user_info['user_name']):
        return USER_NOT_EXIST, None

    # 检查用户输入的密码是否正确
    user_tuple = db.getUser("user_name", user_info['user_name'])
    user = db.tupleToDict(user_tuple, USER_KEY)
    if user_info['password'] != user['password']:
        return WRONG_PASSWORD, None

    # 检查用户是否被激活
    if user['activated'] == 0:
        return USER_NOT_ACTIVATED, None

    # 返回用户的mask
    mask = coder.encode(str(user['id']))

    return LOGIN_SUCCESS, mask


def checkAdminLoginInfo(user_info):
    if user_info['user_name'] != "admin":
        return 1, ""

    if user_info['password'] != "thurec123456":
        return 1, ""

    cur_text = datetime.now().isoformat()
    secret_code = coder.encode(cur_text)
    global admin_secret_code
    admin_secret_code = secret_code
    return 0, secret_code

