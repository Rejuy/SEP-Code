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
        "content_count": raw_info['end'] - raw_info['begin'] + 1
    }
    # 改变filter至函数需要
    if raw_info['course_type'] != 0:
        new_info['filter'].append({"key": "type", "value": raw_info['course_type']})
    if raw_info['course_department'] != 0:
        new_info['filter'].append({"key": "department", "value": raw_info['course_department']})
    # 改变sort_order至函数需要
    new_info['sort_order'] = 'desc'
    # if raw_info['sort_order'] == ASCENDING:
    #     new_info['sort_order'] = ''

    # 改变sort_criteria至函数需要
    if raw_info['course_order'] == 0:
        new_info['sort_criteria'] = 'rate'
    elif raw_info['course_order'] == 1:
        new_info['sort_criteria'] = 'heat'
    elif raw_info['course_order'] == 2:
        new_info['sort_criteria'] = 'time'
    # 获取列表
    raw_list, result = db.getContentList("course_content", new_info)
    new_list = []
    if result:
        new_list = [db.tupleToDict(raw_tuple, BASIC_COURSES_KEY) for raw_tuple in raw_list]
        for content in new_list:
            content['score'] = 2 * content['rate']
            if content['score'] - int(content['score']) >= 0.5:
                pre_star = int(content['score']) + 1
            else:
                pre_star = int(content['score'])
            content['star'] = pre_star / 2
            del content['rate']
            content['tag'] = ''
            content['color'] = COURSE_COLOR[content['type']]
        print(new_list)
    course_count = db.getTableCount("courses")
    return new_list, course_count, result
