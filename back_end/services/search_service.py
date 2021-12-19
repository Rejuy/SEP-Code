from services.mysql_service import db
from headers import *

def globalSearch (info):
    new_info = {
        "like": info['like'],
        "sort_order": "desc",
        "sort_criteria": "star",
        "index_begin": info['begin'],
        "item_count": info['end'] - info['begin'] + 1
    }
    lst, count, flag = db.getGlobalItemList(new_info)
    for i in range(len(lst)):
        lst[i]['tag'] = ''
        if i + info['begin'] + 1 <= 15:
            lst[i]['tag'] = 'TOP' + str(i + info['begin'] + 1)
    return lst, count

def limitedSearch(class_id, like):
    if class_id == 1:
        key_list = BASIC_COURSES_KEY
    elif class_id == 2:
        key_list = BASIC_FOOD_KEY
    elif class_id == 3:
        key_list = BASIC_PLACE_KEY
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
