from mysql_service import db
from code_service import coder
from headers import *


def checkUserExisted(mask):
    user_id = coder.decode(mask)
    return db.checkDataExistence("user", "id", user_id), user_id


def checkItemExisted(raw_info):
    table = INT_TO_TABLE[raw_info['class']]
    return db.checkDataExistence(table, "name", raw_info['name'])


def userAddItem(raw_info, user_id):
    table = INT_TO_TABLE[raw_info['class']]
    raw_info['user_id'] = user_id
    return db.addItem(table, raw_info)

