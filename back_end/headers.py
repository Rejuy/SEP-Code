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
COURSES_KEY = ["id", "name", "teacher", "department", "type", "star", "score", "credit", "comment_count", "heat", "user_id", "activated", "time", "schedule"]
# 插入时所需键值
INSERT_COURSES_KEY = ["name", "teacher", "department", "type", "credit", "star", "score", "comment_count", "heat", "user_id", "activated", "time", "schedule"]
# 返回的key值（基本）
BASIC_COURSES_KEY = ["id", "name", "teacher", "department", "type", "star", "score"]
# 颜色和属性对应
COURSE_COLOR = ["", "#228B22", "#000000", "#FFA500", "#8B4513", "#9400D3", "#FF0000", "#0000FF", "#FF1493"]
# item
ITEM_COURSE_KEY = ["credit", "schedule"]
# 返回给管理员的key
ADMIN_COURSE_KEY = ["id", "name", "teacher", "department", "type", "credit", "time", "activated"]

# food表
# 所有key值
FOOD_KEY = ["id", "name", "position", "scope", "type", "star", "score", "comment_count", "heat", "user_id", "activated", "time", "hours"]
# 插入时所需键值
INSERT_FOOD_KEY = ["name", "position", "scope", "type", "star", "score", "comment_count", "heat", "user_id", "activated", "time", "hours"]
# 返回的key值（基本）
BASIC_FOOD_KEY = ["id", "name", "position", "scope", "type", "star", "score"]
# item
ITEM_FOOD_KEY = ["hours"]
# 返回给管理员的key
ADMIN_FOOD_KEY = ["id", "name", "position", "scope", "type", "time", "activated"]

# place表
# 所有key值
PLACE_KEY = ["id", "name", "position", "type", "star", "score", "comment_count", "heat", "scope", "user_id", "activated", "time", "hours"]
# 插入时所需键值
INSERT_PLACE_KEY = ["name", "position", "scope", "type", "star", "score", "comment_count", "heat", "user_id", "activated", "time", "hours"]
# 返回的key值（基本）
BASIC_PLACE_KEY = ["id", "name", "position", "scope", "type", "star", "score"]
# item
ITEM_PLACE_KEY = ["hours"]
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
GLOBAL_ITEM_KEY = ["id", "title", "description", "star", "score", "scope", "type", "class"]

# 模块
CLASS_TO_INT = {"course": 1, "food": 2, "place": 3}
INT_TO_TABLE = ["", "course_list", "food_list", "place_list"]
INT_TO_BASIC_KEY_LIST = ["", BASIC_COURSES_KEY, BASIC_FOOD_KEY, BASIC_PLACE_KEY]
INT_TO_KEY_LIST = ["", COURSES_KEY, FOOD_KEY, PLACE_KEY]

# hash
course_scope_table = ['任意院系','车辆学院','材料学院','电机系','电子系','法学院','工物系','公管学院','工业工程系','航院','化学系','化工系','环境学院','机械系','经管学院','金融学院','建筑学院','计算机系','交叉信息院','集成电路学院','美术学院','马克思主义学院','能动系','求真书院','清华-伯克利深圳学院','日新书院','软件学院','人文学院','数学系','水利系','社科学院','生命学院','苏世民书院','土木系','体育部','土水学院','外文系','物理系','未央书院','新雅书院','行健书院','新闻学院','训练中心','医学院','药学院','语言中心','艺教中心','致理书院','自动化系','其他开课单位',]

course_type_table = ['全部课程','专业课','数理课','外文课','实验课','体育课','思政课','文核课','文素课','实践课',]

course_schedule_table = ["", "春季学期", "夏季学期", "秋季学期", "春、秋学期"]

food_scope_table = ['', '校内餐饮', '校外餐饮']

inside_food_type_table = ['','家园','甲所','寓园','融园','澜园','荷园','北园','南园','桃李园','紫荆园','清芬园','听涛园','观畴园','玉树园','芝兰园','丁香园','熙春园','清真食堂',]

outside_food_type_table = ['','汉堡披萨','龙虾烧烤','香锅火锅','米线拉面','日韩料理','简餐便当','各类饮品',]

place_scope_table = ['','校内地点', '校外地点']

place_type_table = ['', '自习场所', '锻炼场所', '会议场所', '娱乐场所']



import datetime
start_date = datetime.datetime.now()
