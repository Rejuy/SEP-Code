import re
from headers import *
from services.mysql_service import db


def checkLoginInfo(user_info):
    # 检查用户输入的用户名是否存在
    if not db.checkUserNameExistence(user_info['user_name']):
        return USER_NOT_EXIST, None

    # 检查用户输入的密码是否正确
    user_tuple = db.getUser("user_name", user_info['user_name'])
    user = {}
    # 将元组转化为字典
    print(user_tuple)
    for i in range(USER_KEY_AMOUNT):
        user[USER_KEY[i]] = user_tuple[i]
        print(i)
    print(user)
    if user_info['password'] != user['password']:
        return WRONG_PASSWORD, None

    return LOGIN_SUCCESS, user

