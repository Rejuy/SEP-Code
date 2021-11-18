from headers import *
from services.mysql_service import db
from services.code_service import coder


def getCoursesList(raw_info):
    '''
    :param raw_info:{
        filter;
        filter_value;
        sort_order;
        sort_criteria;
        index_begin;
        content_count;
    }
    :return: list<dict>
    '''
    new_info = {
        "key_list": BASIC_COURSES_KEY,
        "filter": "",
        "filter_value": raw_info['filter_value'],
        "sort_order": "not_sort",
        "sort_criteria": "",
        "index_begin": raw_info['index_begin'],
        "content_count": raw_info['content_count']
    }
    # 改变filter至函数需要
    if raw_info['filter'] == COURSE_TYPE:
        new_info['filter'] = 'type'
    elif raw_info['filter'] == COURSE_DEPARTMENT:
        new_info['filter'] = 'department'
    # 改变sort_order至函数需要
    if raw_info['sort_order'] == ASCENDING:
        new_info['sort_order'] = ''
    elif raw_info['sort_order'] == DESCENDING:
        new_info['sort_order'] = 'desc'
    # 改变sort_criteria至函数需要
    if raw_info['sort_criteria'] == RATE_ORDER:
        new_info['sort_criteria'] = 'rate'
    elif raw_info['sort_criteria'] == HEAT_ORDER:
        new_info['sort_criteria'] = 'heat'
    elif raw_info['sort_criteria'] == RATE_COUNT_ORDER:
        new_info['sort_criteria'] = 'rate_count'
    elif raw_info['sort_criteria'] == COMMENT_COUNT_ORDER:
        new_info['sort_criteria'] = 'comment_count'
    # 获取列表
    raw_list, result = db.getContentList("course_content", new_info)
    new_list = []
    if result:
        new_list = [db.tupleToDict(raw_tuple, BASIC_COURSES_KEY) for raw_tuple in raw_list]
        for content in new_list:
            content['mask'] = coder.encode(str(content['id']))
            del content['id']
        print(new_list)
    return new_list, result
