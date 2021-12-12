from services.mysql_service import db
import json

def getCommentsByName (user_name, offset, size):
    info = {
        'key_list': ['user', 'text', 'image', 'star', 'time', 'likes', 'item_id', 'class'],
        'filter': [{'key': 'user', 'value': user_name}],
        'sort_order': 'not_sort',
        'index_begin': offset,
        'content_count': size
    }
    commentState = db.getItemList('comment', info)
    # print(commentState[1])
    commentList = commentState[0]
    for i in range(len(commentList)):
        commentList[i] = dict(zip(info['key_list'], commentList[i]))
        # print(commentList[i]['image'], type(commentList[i]['image']))
        commentList[i]['image'] = json.loads(commentList[i]['image'])
        # print(commentList[i]['image'], type(commentList[i]['image']))
    return commentList

def getCommentsByItem (class_id, item_id):
    info = {
        'key_list': ['user', 'text', 'image', 'star', 'time', 'likes'],
        'filter': [{'key': 'class', 'value': class_id}, {'key': 'item_id', 'value': item_id}],
        'sort_order': 'not_sort',
        'index_begin': 0,
        'content_count': 500
    }
    commentState = db.getItemList('comment', info)
    # print(commentState[1])
    commentList = commentState[0]
    for i in range(len(commentList)):
        commentList[i] = dict(zip(info['key_list'], commentList[i]))
        # print(commentList[i]['image'], type(commentList[i]['image']))
        commentList[i]['image'] = json.loads(commentList[i]['image'])
        # print(commentList[i]['image'], type(commentList[i]['image']))
    return commentList