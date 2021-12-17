from services.mysql_service import db
from headers import *

def globalSearch (like):
    info = {
        "like": like,
        "sort_order": "desc",
        "sort_criteria": "star",
        "index_begin": 0,
        "item_count": 500
    }
    lst = db.getGlobalItemList(info)[0]
    return lst

def limitedSearch(class_id, like):
    key_list = INT_TO_KEY_LIST[class_id]
    table = INT_TO_TABLE[class_id]

    info = {
        "like": like,
        "key_list": key_list,
        "sort_order": "desc",
        "sort_criteria": "star",
        "index_begin": 0,
        "item_count": 500,
        "filter": []
    }
    lst = db.getItemList(table, info)[0]
    # print(lst)
    for i in range(len(lst)):
        lst[i] = dict(zip(key_list, lst[i]))
    return lst