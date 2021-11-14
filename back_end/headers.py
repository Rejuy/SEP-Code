BAD_ARGUMENTS = -1  # 参数错误

# 注册界面返回值
INVALID_EMAIL = 1  # 邮箱不合法
INVALID_USERNAME = 2  # 用户名不合法
INVALID_PASSWORD_LENGTH = 3  # 密码长度不合法
INVALID_PASSWORD_MISSING_TYPE = 4  # 密码符号类型不足
INVALID_PASSWORD_ILLEGAL_TYPE = 5  # 密码包含非法字符
EMAIL_EXIST = 6  # 邮箱已存在
USERNAME_EXIST = 7  # 用户名已存在
VALID_INFO = 0  # 信息合法

# 登陆页面返回值
USER_NOT_EXIST = 1  # 不存在的用户名
WRONG_PASSWORD = 2  # 错误的密码
LOGIN_SUCCESS = 0  # 登录成功

# user表所有key值
USER_KEY = ["id", "user_name", "password", "email", "account_birth", "collection_count", "like_count", "comment_count", "content_count", "activated", "introduction"]
USER_KEY_AMOUNT = 11
