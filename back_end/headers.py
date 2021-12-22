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
USER_KEY = ["id", "user_name", "password", "email", "account_birth", "collection_count", "like_count", "comment_count", "item_count", "activated", "introduction", "image"]
# 插入时所需键值
INSERT_USER_KEY = ["user_name", "password", "email", "account_birth", "collection_count", "like_count", "comment_count", "item_count", "activated"]
# 获取user表的时候所需的键值
ADMIN_GET_USER_KEY = ['id', 'user_name', 'email', 'account_birth', 'collection_count', 'like_count', 'comment_count', 'item_count', 'activated', "image"]
# 管理员端修改用户所需的list
ADMIN_UPDATE_USER_KEY = ["user_name", "email", "activated", "image"]

# courses表
# 所有key值
COURSES_KEY = ["id", "name", "teacher", "department", "type", "credit", "star", "score", "comment_count", "heat", "user_id", "activated", "time", "schedule"]
# 插入时所需键值
INSERT_COURSES_KEY = ["name", "teacher", "department", "type", "credit", "star", "score", "comment_count", "heat", "user_id", "activated", "time", "schedule"]
# 返回的key值（基本）
BASIC_COURSES_KEY = ["id", "name", "teacher", "department", "type", "star", "score"]
# 颜色和属性对应
COURSE_COLOR = ["", "#228B22", "#000000", "#FFA500", "#8B4513", "#9400D3", "#FF0000", "#0000FF", "#FF1493"]
# item
ITEM_COURSE_KEY = ["name", "teacher", "department", "type", "star", "credit", "schedule"]
# 返回给管理员的key
ADMIN_COURSE_KEY = ["id", "name", "teacher", "department", "type", "credit", "time", "activated"]

# food表
# 所有key值
FOOD_KEY = ["id", "name", "position", "scope", "type", "star", "score", "comment_count", "heat", "user_id", "activated", "time", "hours"]
# 插入时所需键值
INSERT_FOOD_KEY = ["name", "position", "scope", "type", "star", "score", "comment_count", "heat", "user_id", "activated", "time", "hours"]
# 返回的key值（基本）
BASIC_FOOD_KEY = ["id", "name", "position", "scope", "type", "star", "score", "hours"]
# item
ITEM_FOOD_KEY = ["name", "position", "scope", "star"]
# 返回给管理员的key
ADMIN_FOOD_KEY = ["id", "name", "position", "scope", "type", "time", "activated"]

# place表
# 所有key值
PLACE_KEY = ["id", "name", "position", "scope", "type", "star", "score", "comment_count", "heat", "user_id", "activated", "time", "hours"]
# 插入时所需键值
INSERT_PLACE_KEY = ["name", "position", "scope", "type", "star", "score", "comment_count", "heat", "user_id", "activated", "time", "hours"]
# 返回的key值（基本）
BASIC_PLACE_KEY = ["id", "name", "position", "scope", "type", "star", "score", "hours"]
# item
ITEM_PLACE_KEY = ["name", "position", "scope", "star"]
# 返回给管理员的key
ADMIN_PLACE_KEY = ["id", "name", "position", "scope", "type", "time", "activated"]

# comment
# 插入时所需key值
INSERT_COMMENT_KEY = ["class", "item_id", "user", "star", "time", "likes", "text", "image", "upper_comment_id", "lower_comment_count"]
# 所有key值
COMMENT_KEY = ["id", "class", "item_id", "user", "star", "time", "likes", "text", "image", "upper_comment_id", "lower_comment_count"]
# 获取时的key
BASIC_USER_COMMENT_KEY = ["id", "class", "item_id", "star", "time", "likes", "text", "image", "upper_comment_id", "lower_comment_count"]
# item获取的comment_key
ITEM_COMMENT_KEY = ["id", "user", "star", "time", "likes", "text"]

# like
# 插入时所需key值
INSERT_LIKE_KEY = ["user", "comment_id", "time"]
# 所有key值
LIKE_KEY = ["id", "user", "comment_id", "time"]

# collection
# 插入时所需key值
INSERT_COLLECTION_KEY = ["user_id", "class", "item_id", "time", "item_name"]
# 所有key值
COLLECTION_KEY = ["id", "user_id", "class", "item_id", "time", "item_name"]

# 模块global获取的item键
GLOBAL_ITEM_KEY = ["id", "title", "description", "star", "score", "class"]

# 模块
CLASS_TO_INT = {"course": 1, "food": 2, "place": 3}
INT_TO_TABLE = ["", "course_list", "food_list", "place_list"]
INT_TO_BASIC_KEY_LIST = ["", BASIC_COURSES_KEY, BASIC_FOOD_KEY, BASIC_PLACE_KEY]
INT_TO_KEY_LIST = ["", COURSES_KEY, FOOD_KEY, PLACE_KEY]