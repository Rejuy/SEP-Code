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


def adminGetItemList(raw_info):
    # 获得键值
    if raw_info['class'] == 1:
        key_list = ADMIN_COURSE_KEY
    elif raw_info['class'] == 2:
        key_list = ADMIN_FOOD_KEY
    elif raw_info['class'] == 3:
        key_list = ADMIN_PLACE_KEY
    else:
        return [], False
    # 构造info
    info = {
        "key_list": key_list,
        "filter": [
            #{
             #   "key": "activated",
              #  "value": 0
            #}
        ],
        "like": "",
        "sort_order": "not_sort",
        "sort_criteria": "",
        "index_begin": raw_info['offset'],
        "item_count": raw_info['size']
    }
    print(61)
    item_list, count, flag = db.getItemList(INT_TO_TABLE[raw_info['class']], info)
    for i in range(len(item_list)):
        item_list[i] = db.tupleToDict(item_list[i], key_list)
        item_list[i]['time'] = db.timeToStr(item_list[i]['time'])
    return item_list, flag


def operateItem(raw_info):
    try:
        table = INT_TO_TABLE[raw_info['class']]
    except Exception as e:
        print("Error in <add_item_service.checkItemExisted>")
        print(e)
        return "error"
    # 判断操作
    if raw_info['operation'] == 0:
        # 删除item
        if db.delItem(table, ["id"], [raw_info['id']], 0):
            return 0
    elif raw_info['operation'] == 1:
        # 激活item
        if db.updateData(table, "id", raw_info['id'], "activated", 1):
            class_name = table.split("_")[0][0].upper() + table.split("_")[0][1:]
            db.selfChangeData("class", ["name"], [class_name], "count", 1)
            result, flag = db.getData(table, ["id"], [raw_info["id"]], ["user_id"])
            user_id = result[0]['user_id']
            db.selfChangeData("user", ["id"], [user_id], "item_count", 1)
            return 1
    return -1


def editUser(raw_info):
    if raw_info['delete']:
        # delete user
        return db.delUser("id", raw_info['user']['id'])
    else:
        # edit user
        for key in raw_info['user'].keys():
            if key == "id":
                continue
            if not db.updateData("user", "id", raw_info['user']['id'], key, raw_info['user'][key]):
                return False
        return True


def getSingleUser(id):
    user = db.getUser("id", id)
    if not user:
        return None
    user = db.tupleToDict(user, USER_KEY)
    del user['password']
    del user['introduction']
    user['account_birth'] = db.timeToStr(user['account_birth'])
    return user


def getSingleItem(raw_info):
    # 获得键值
    if raw_info['class'] == 1:
        key_list = ADMIN_COURSE_KEY
    elif raw_info['class'] == 2:
        key_list = ADMIN_FOOD_KEY
    elif raw_info['class'] == 3:
        key_list = ADMIN_PLACE_KEY
    else:
        return None, False
    return db.getData(INT_TO_TABLE[raw_info['class']], ["id"], [raw_info['id']], key_list, get_all=False)


def editItem(raw_info):
    """
    if raw_info['class'] == 1:
        key_list = ADMIN_COURSE_KEY
    elif raw_info['class'] == 2:
        key_list = ADMIN_FOOD_KEY
    elif raw_info['class'] == 3:
        key_list = ADMIN_PLACE_KEY

        """
    try:
        table = INT_TO_TABLE[raw_info['class']]
    except Exception as e:
        print("Error in <add_item_service.checkItemExisted>")
        print(e)
        return "error"
    if raw_info['delete']:
        # delete item
        item_activated = db.getData(table, ["id"], [raw_info['item']['id']], ["activated"])
        return db.delItem(table, ["id"], [raw_info['item']['id']], item_activated)
    else:
        # edit item
        for key in raw_info['item'].keys():
            if key == "id":
                continue
            if not db.updateData(table, "id", raw_info['item']['id'], key, raw_info['item'][key]):
                return False
            print(146)
        return True


def editComment(raw_info):
    if raw_info['delete']:
        # delete item
        return db.delComment("id", raw_info['comment']['id'])
    else:
        # edit item
        for key in raw_info['comment'].keys():
            if key == "id":
                continue
            if not db.updateData("comment", "id", raw_info['comment']['id'], key, raw_info['comment'][key]):
                return False
        return True


