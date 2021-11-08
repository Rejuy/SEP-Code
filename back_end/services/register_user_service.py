import re
from headers import *


def checkUserInfo(user_info):
    # 检查用户信息是否合法
    # 检查用户邮箱是否合法
    if not re.match(r"^[0-9A-Za-z-_]*$", user_info['email']):
        return INVALID_EMAIL

    # 检查用户名是否合法
    if len(user_info['user_name']) < 6 or len(user_info['user_name']) > 10:
        return INVALID_USERNAME

    # 检查用户密码是否合法
    if len(user_info['password']) < 6 or len(user_info['password']) > 18:
        return INVALID_PASSWORD_LENGTH

    if not re.match(r"((?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).*$)", user_info['password']):
        return INVALID_PASSWORD_MISSING_TYPE

    if not re.match(r"^[0-9A-Za-z@#$%^&*]*$", user_info['password']):
        return INVALID_PASSWORD_ILLEGAL_TYPE

    # TODO:
    #  检查数据库中是否已经存在邮箱和用户名

    # 合法
    # TODO:
    #  向用户邮箱发送请求，将用户信息写入数据库，并设置其激活状态为否

    return VALID_INFO


