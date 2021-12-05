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
USER_NOT_ACTIVATED = 3  # 用户未激活
LOGIN_SUCCESS = 0  # 登录成功

# 课程模块======
# filter种类
COURSE_DEFAULT = 0  # 不筛选
COURSE_TYPE = 1  # 按课程类型筛选
COURSE_DEPARTMENT = 2  # 按开课院系筛选

# 排序种类
DEFAULT_ORDER = 0  # 数据库原始顺序
ASCENDING = 1  # 升序
DESCENDING = 2  # 降序

# 排序标准
RATE_ORDER = 1  # 按评分排序
HEAT_ORDER = 2  # 按热度排序
RATE_COUNT_ORDER = 3  # 按评分数量排序
COMMENT_COUNT_ORDER = 4  # 按评论数量排序

# user表
# 所有key值
USER_KEY = ["id", "user_name", "password", "email", "account_birth", "collection_count", "like_count", "comment_count", "content_count", "activated", "introduction"]
# 插入时所需键值
INSERT_USER_KEY = ["user_name", "password", "email", "account_birth", "collection_count", "like_count", "comment_count", "content_count", "activated"]

# courses表
# 所有key值
COURSES_KEY = ["id", "number", "type", "name", "teacher", "credit", "department", "schedule", "rate_count", "rate", "comment_count", "heat"]
# 插入时所需键值
INSERT_COURSES_KEY = ["number", "type", "name", "teacher", "credit", "department", "schedule", "rate_count", "rate", "comment_count", "heat"]
# 返回的key值（基本）
BASIC_COURSES_KEY = ["id", "name", "teacher", "department", "type", "rate"]
# 颜色和属性对应
COURSE_COLOR = ["", "#228B22", "#000000", "#FFA500", "#8B4513", "#9400D3", "#FF0000", "#0000FF", "#FF1493"]

# item
ITEM_COURSE_KEY = ["name", "teacher", "department", "type", "rate", "credit"]

# comment
INSERT_COMMENT_KEY = ["class", "content_id", "from_user_id", "like_count", "upper_comment_id", "lower_comment_count", "time", "star", "text", "deleted"]
COMMENT_KEY = ["id", "class", "content_id", "from_user_id", "like_count", "upper_comment_id", "lower_comment_count", "time", "star", "text", "deleted"]

