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

# 课程种类
TYPE_SUBJECT_DISCUSSION = 1  # 专题研讨课
TYPE_TOTAL_FOREIGN_LANGUAGE = 2  # 全外文授课
TYPE_PUBLIC_ENGLISH = 3  # 公共英语
TYPE_50_PERCENT_FOREIGN_LANGUAGE = 4  # 外文授课比例>=50%
TYPE_FOREIGN_LANGUAGE_MATERIAL = 5  # 外文教材，中文为主进行授课
TYPE_PRACTICE = 6  # 实践课
TYPE_EXPERIMENT = 7  # 实验课
TYPE_CHALLENGE = 8  # 挑战性学习课程
TYPE_CULTURE_CORE = 9  # 文化素质核心课
TYPE_CULTURE = 10  # 文化素质课
TYPE_ROOKIE_DISCUSSION = 11  # 新生研讨课
TYPE_ROOKIE_DISCUSSION_CLASS = 12  # 新生研讨课（大类）
TYPE_MIXTURE = 13  # 融合式教学
TYPE_FINE = 14  # 精品课
TYPE_ENGLISH_MAJOR = 15  # 英语专业
TYPE_FOREIGN_LANGUAGE_ACKNOWLEDGED = 16  # 认证外文课
TYPE_GENERAL_ENGLISH = 17  # 通识英语
TYPE_GENERAL_HONOR = 18  # 通识荣誉课
TYPE_GENERAL_ELECTIVE = 19  # 通识选修课

# 院系种类
DEPARTMENT_ARCHITECTURE = 1  # 建筑学院
DEPARTMENT_CITY_DESIGN = 2  # 城规系
DEPARTMENT_CIVIL_ENGINEERING = 3  # 土木系
DEPARTMENT_WATER_RESOURCES = 4  # 水利系
DEPARTMENT_ENVIRONMENT = 5  # 环境学院
DEPARTMENT_MECHANISM = 6  # 机械系
DEPARTMENT_PRECISION_INSTRUMENT = 7  # 精仪系
DEPARTMENT_ENERGY = 8  # 能动系
DEPARTMENT_VEHICLE = 9  # 车辆学院
DEPARTMENT_INDUSTRY = 10  # 工业工程
DEPARTMENT_INFORMATION = 11  # 信息学院
DEPARTMENT_ELECTRICAL_ENGINEERING = 12  # 电机系
DEPARTMENT_ELECTRONIC_ENGINEERING = 13  # 电子系
DEPARTMENT_COMPUTER = 14  # 计算机系
DEPARTMENT_AUTOMATIZATION = 15  # 自动化系
DEPARTMENT_INTEGRATE_CIRCUIT = 16  # 集成电路学院
DEPARTMENT_AIR = 17  # 航院
DEPARTMENT_ENGINEERING_PHYSICS = 18  # 工物系
DEPARTMENT_CHEMISTRY_ENGINEERING = 19  # 化工系
DEPARTMENT_MATERIAL = 20  # 材料学院
DEPARTMENT_MATH = 21  # 数学系
DEPARTMENT_PHYSICS = 22  # 物理系
DEPARTMENT_CHEMISTRY = 23  # 化学系
DEPARTMENT_LIFE = 24  # 生命学院
DEPARTMENT_EARTH = 25  # 地学系
DEPARTMENT_CROSS_INFORMATION = 26  # 交叉信息院
DEPARTMENT_HIGH_EXPERIMENT = 27  # 高研院
DEPARTMENT_ECONOMICS = 28  # 经管学院
DEPARTMENT_PUBLIC = 29  # 公管学院
DEPARTMENT_FINANCE = 30  # 金融学院
DEPARTMENT_FOREIGN_LANGUAGE = 31  # 外文系
DEPARTMENT_LAW = 32  # 法学院
DEPARTMENT_NEWS = 33  # 新闻学院
DEPARTMENT_MARX = 34  # 马克思主义学院
DEPARTMENT_CULTURE = 35  # 人文学院
DEPARTMENT_SOCIETY = 36  # 社科学院
DEPARTMENT_SPORT = 37  # 体育部
DEPARTMENT_LIBRARY = 38  # 图书馆
DEPARTMENT_ART_EDUCATION = 39  # 艺教中心
DEPARTMENT_ART = 40  # 美术学院
DEPARTMENT_SOIL_WATER = 41  # 土水学院
DEPARTMENT_CONSTRUCTION_MANAGEMENT = 42  # 建管系
DEPARTMENT_ASTRONOMY = 43  # 天文系
DEPARTMENT_HEALTH = 44  # 卫健学院
DEPARTMENT_SU = 45  # 苏市民书院
DEPARTMENT_ARCHITECTURE_TECHNIQUE = 46  # 建筑技术
DEPARTMENT_NUCLEUS = 47  # 核研院
DEPARTMENT_EDUCATION = 48  # 教研院
DEPARTMENT_TRAIN = 49  # 训练中心
DEPARTMENT_EEEE = 50  # 电工电子中心
DEPARTMENT_STUDENT = 51  # 学生部
DEPARTMENT_ARMED = 52  # 武装部
DEPARTMENT_EDUCATION_ADMINISTRATION = 53  # 教务处
DEPARTMENT_GRADUATE = 54  # 研究生院
DEPARTMENT_SHENZHEN = 55  # 深研院
DEPARTMENT_HOSPITAL = 56  # 校医院
DEPARTMENT_MEDICAL = 57  # 医学院
DEPARTMENT_MEDICINE = 58  # 药学院
DEPARTMENT_SOFTWARE = 59  # 软件学院
DEPARTMENT_NET = 60  # 网络研究院
DEPARTMENT_REGION = 61  # 地区研究院
DEPARTMENT_AIR_TRAVEL = 62  # 航发院
DEPARTMENT_LANGUAGE = 63  # 语言中心
DEPARTMENT_XINYA = 64  # 新雅书院
DEPARTMENT_RIXIN = 65  # 日新书院
DEPARTMENT_WEIYANG = 66  # 未央书院
DEPARTMENT_XINGJIAN = 67  # 行健书院
DEPARTMENT_QIUZHEN = 68  # 求真书院
DEPARTMENT_INTERNATIONAL_GRADUATE = 69  # 国际研究生院
DEPARTMENT_BERKELEY = 70  # 清华-伯克利深圳学院
DEPARTMENT_INTERNATIONAL_INNOVATION = 71  # 清华大学全球创新学院

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
# 添加评论
INSERT_COMMENT_KEY = ["class", "content_id", "from_user_id", "like_count", "upper_comment_id", "lower_comment_id", "time", "star", "text", "deleted", "imageurl"]
# 返回的key值（基本）
BASIC_COURSES_KEY = ["id", "name", "teacher", "rate"]