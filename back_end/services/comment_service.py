from services.mysql_service import db
import json

def getTitle (item_class, item_id):
    table = "course_list"
    if (item_class == 2):
        table = "food_list"
    elif (item_class == 3):
        table = "place_list"
    return db.getData(table, ["id"], [item_id], ["name"])[0][0]["name"]

def getCommentsByName (user_name, offset, size):
    info = {
        'key_list': ['class', 'item_id', 'user', 'text', 'image', 'star', 'time', 'likes'],
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
        commentList[i]['image'] = json.loads(commentList[i]['image'])
        commentList[i]['item_title'] = getTitle(commentList[i]['class'], commentList[i]['item_id'])
    return commentList

def getCommentsByItem (class_id, item_id):
    info = {
        'key_list': ['class', 'item_id', 'user', 'text', 'image', 'star', 'time', 'likes'],
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
        commentList[i]['image'] = json.loads(commentList[i]['image'])
        commentList[i]['item_title'] = getTitle(commentList[i]['class'], commentList[i]['item_id'])
    return commentList

def getCommentsByComment (comment_id):
    info = {
        'key_list': ['user', 'text', 'image', 'time', 'likes'],
        'filter': [{'key': 'upper_comment_id', 'value': comment_id}],
        'sort_order': 'not_sort',
        'index_begin': 0,
        'content_count': 500
    }
    commentState = db.getItemList('comment', info)
    # print(commentState[1])
    commentList = commentState[0]
    for i in range(len(commentList)):
        commentList[i] = dict(zip(info['key_list'], commentList[i]))
        commentList[i]['image'] = json.loads(commentList[i]['image'])
    return commentList