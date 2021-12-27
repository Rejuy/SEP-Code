from headers import *
from services.mysql_service import db
from services.code_service import coder


def getCoursesList(raw_info):
    '''
    :param raw_info:{
        course_type: ...; # 课程类型
        course_department: ...; # 开课院系
        course_order: ...; # 排序方式
        begin: ...;
        end: ...;
    }
    :return: list<dict>
    '''
    new_info = {
        "key_list": BASIC_COURSES_KEY,
        "filter": [],
        "sort_order": "not_sort",
        "sort_criteria": "",
        "index_begin": raw_info['begin'],
        "item_count": raw_info['end'] - raw_info['begin'] + 1
    }
    # 改变filter至函数需要
    if raw_info['course_type'] != 0:
        new_info['filter'].append({"key": "type", "value": raw_info['course_type']})
    if raw_info['course_department'] != 0:
        new_info['filter'].append({"key": "department", "value": raw_info['course_department']})
    if raw_info['mask'] != "":
        new_info['filter'].append({"key": "user_id", "value": coder.decode(raw_info['mask'])})
    # 改变sort_order至函数需要
    new_info['sort_order'] = 'desc'
    # if raw_info['sort_order'] == ASCENDING:
    #     new_info['sort_order'] = ''

    # 改变sort_criteria至函数需要
    if raw_info['course_order'] == 0:
        new_info['sort_criteria'] = 'star'
    elif raw_info['course_order'] == 1:
        new_info['sort_criteria'] = 'heat'
    elif raw_info['course_order'] == 2:
        new_info['sort_criteria'] = 'time'

    if raw_info['like'] != "":
        new_info['like'] = raw_info['like']
    print('47', new_info)
    # 获取列表
    raw_list, course_count, result = db.getItemList("course_list", new_info)
    new_list = []
    if result:
        new_list = [db.tupleToDict(raw_tuple, BASIC_COURSES_KEY) for raw_tuple in raw_list]
        for i in range(len(new_list)):
            new_list[i]['tag'] = ''
            if i + raw_info['begin'] + 1 <= 15:
                new_list[i]['tag'] = 'TOP' + str(i + raw_info['begin'] + 1)
            # new_list[i]['color'] = COURSE_COLOR[new_list[i]['type']]
        print(new_list)
    # course_count = db.getTableCount("course_list")
    return new_list, course_count, result


def getCourseItem(info):
    info["count"] = info['end'] - info['begin'] + 1
    item, flag = db.getItem("course_list", 1, info, ITEM_COURSE_KEY)
    return item, flag


def getFullContent(id):
    return db.getData("comment", ["id"], [id], ["text"], get_all=False)
