from headers import *
from services.mysql_service import db


def getPlacesList(raw_info):
    '''
    :param raw_info:{
        place_type: ...; # 餐饮类型
        place_scope: ...; # 餐饮位置（校内或校外）
        place_order: ...; # 排序方式
        begin: ...;
        end: ...;
    }
    :return: list<dict>
    '''
    new_info = {
        "key_list": BASIC_PLACE_KEY,
        "filter": [],
        "sort_order": "not_sort",
        "sort_criteria": "",
        "index_begin": raw_info['begin'],
        "item_count": raw_info['end'] - raw_info['begin'] + 1
    }
    # 改变filter至函数需要
    if raw_info['place_type'] != 0:
        new_info['filter'].append({"key": "type", "value": raw_info['place_type']})
    if raw_info['place_scope'] != 0:
        new_info['filter'].append({"key": "scope", "value": raw_info['place_scope']})
    # 改变sort_order至函数需要
    new_info['sort_order'] = 'desc'
    # if raw_info['sort_order'] == ASCENDING:
    #     new_info['sort_order'] = ''

    # 改变sort_criteria至函数需要
    if raw_info['place_order'] == 1:
        new_info['sort_criteria'] = 'heat'
    elif raw_info['place_order'] == 2:
        new_info['sort_criteria'] = 'time'
    else:
        new_info['sort_criteria'] = 'star'

    if "like" in raw_info.keys():
        new_info['like'] = raw_info['like']
    
    # 获取列表
    raw_list, place_count, result = db.getItemList("place_list", new_info)
    if result:
        new_list = [db.tupleToDict(raw_tuple, BASIC_PLACE_KEY) for raw_tuple in raw_list]
        for i in range(len(new_list)):
            new_list[i]['tag'] = ''
            if i + raw_info['begin'] + 1 <= 15:
                new_list[i]['tag'] = 'TOP' + str(i + raw_info['begin'] + 1)
        print(new_list)
    # place_count = db.getTableCount("place_list")
    return new_list, place_count, result


def getPlaceItem(id):
    item, flag = db.getItem("place_list", 3, id, ITEM_PLACE_KEY)
    return item, flag
