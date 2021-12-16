from services.mysql_service import db
from services.login_service import admin_secret_code
from headers import *


def checkSecretCode(secret_code):
    if admin_secret_code != secret_code:
        return False
    return True


def getUserCount():
    return db.getTableCount("user")


def getUserList(info):
    """
    :param info: {
        "offset":,
        "size":
    }
    :return: list<user>
    """
    return db.getUserList(info)


def getInactivatedItemList(raw_info):
    # 获得键值
    if raw_info['class'] == 1:
        key_list = ADMIN_COURSE_KEY
    elif raw_info['class'] == 2:
        key_list = ADMIN_FOOD_KEY
    elif raw_info['class'] == 3:
        key_list = ADMIN_PLACE_KEY
    else:
        return [], False
    # 获得排序方式
    if raw_info['order'] == 0:
        order = "not_sort"
    elif raw_info['order'] == 1:
        order = "asc"
    elif raw_info['order'] == 2:
        order = "desc"
    else:
        order = ""
    # 构造info
    info = {
        "key_list": key_list,
        "filter": [
            {
                "key": "activated",
                "value": 0
            }
        ],
        "like": "",
        "sort_order": order,
        "sort_criteria": "time",
        "index_begin": raw_info['offset'],
        "item_count": raw_info['size']
    }
    item_list, flag = db.getItemList(INT_TO_TABLE[raw_info['class']], info)
    for i in range(len(item_list)):
        item_list[i] = db.tupleToDict(item_list[i], key_list)
        item_list[i]['time'] = db.timeToStr(item_list[i]['time'])
    return item_list, flag
