from services.mysql_service import db
import json

def getCommentsByName (user_name, offset, size):
    info = {
        'key_list': ['user', 'text', 'image', 'time', 'likes', 'item_id'],
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