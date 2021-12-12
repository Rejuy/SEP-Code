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
    lst = db.getGlobalItemList(info)
    return lst

def limitedSearch(table, like):
    key_list = ["star"]
    if table == "food_list":
        key_list = FOOD_KEY
    elif table == "place_list":
        key_list = PLACE_KEY
    elif table == "course_list":
        key_list = COURSES_KEY

    info = {
        "like": like,
        "key_list": key_list,
        "sort_order": "desc",
        "sort_criteria": "star",
        "index_begin": 0,
        "content_count": 500,
        "filter": []
    }
    lst = db.getItemList(table, info)[0]
    for i in range(len(lst)):
        lst[i] = dict(zip(key_list, lst[i]))
    return lst