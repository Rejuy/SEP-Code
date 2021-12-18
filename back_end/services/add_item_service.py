from services.mysql_service import db
from services.code_service import coder
from headers import *


def checkUserExisted(mask):
    user_id = coder.decode(mask)
    return db.checkDataExistence("user", "id", user_id), user_id


def checkItemExisted(raw_info):
    try:
        table = INT_TO_TABLE[raw_info['class']]
    except Exception as e:
        print("Error in <add_item_service.checkItemExisted>")
        print(e)
        return "error"
    return db.checkDataExistence(table, "name", raw_info['info']['name'])


def userAddItem(raw_info, user_id):
    try:
        table = INT_TO_TABLE[raw_info['class']]
    except Exception as e:
        print("Error in <add_item_service.userAddItem>")
        print(e)
        return "error"
    raw_info['info']['user_id'] = user_id
    return db.addItem(table, raw_info['info'])

