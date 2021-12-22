from headers import *
from services.mysql_service import db


def getFoodsList(raw_info):
    '''
    :param raw_info:{
        food_type: ...; # 餐饮类型
        food_scope: ...; # 餐饮位置（校内或校外）
        food_order: ...; # 排序方式
        begin: ...;
        end: ...;
    }
    :return: list<dict>
    '''
    new_info = {
        "key_list": BASIC_FOOD_KEY,
        "filter": [],
        "sort_order": "not_sort",
        "sort_criteria": "",
        "index_begin": raw_info['begin'],
        "item_count": raw_info['end'] - raw_info['begin'] + 1
    }
    # 改变filter至函数需要
    if raw_info['food_type'] != 0:
        new_info['filter'].append({"key": "type", "value": raw_info['food_type']})
    if raw_info['food_scope'] != 0:
        new_info['filter'].append({"key": "scope", "value": raw_info['food_scope']})
    # 改变sort_order至函数需要
    new_info['sort_order'] = 'desc'
    # if raw_info['sort_order'] == ASCENDING:
    #     new_info['sort_order'] = ''

    # 改变sort_criteria至函数需要
    if raw_info['food_order'] == 1:
        new_info['sort_criteria'] = 'heat'
    elif raw_info['food_order'] == 2:
        new_info['sort_criteria'] = 'time'
    else:
        new_info['sort_criteria'] = 'star'

    if raw_info['like'] != "":
        new_info['like'] = raw_info['like']

    # 获取列表
    raw_list, food_count, result = db.getItemList("food_list", new_info)
    if result:
        new_list = [db.tupleToDict(raw_tuple, BASIC_FOOD_KEY) for raw_tuple in raw_list]
        for i in range(len(new_list)):
            new_list[i]['tag'] = ''
            if i + raw_info['begin'] + 1 <= 15:
                new_list[i]['tag'] = 'TOP' + str(i + raw_info['begin'] + 1)
        print(new_list)
    # food_count = db.getTableCount("food_list")
    return new_list, food_count, result



def getFoodItem(info):
    info["count"] = info['end'] - info['begin'] + 1
    item, flag = db.getItem("food_list", 2, info, ITEM_FOOD_KEY)
    return item, flag
