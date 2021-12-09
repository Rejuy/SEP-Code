from headers import *
from services.mysql_service import db


def modifyUserLike(raw_info):
    """
    :param raw_info:{
        user:
        comment_id:
        operation: 1点赞，2删除点赞
    }
    :return: bool
    """
    liked = db.checkCommentLiked(raw_info['user'], raw_info['comment_id'])
    if raw_info['operation'] == 1:
        if liked:
            return False
        db.addLike(raw_info['user'], raw_info['comment_id'])
    elif raw_info['operation'] == 0:
        if not liked:
            return False
        db.delLike(raw_info['user'], raw_info['comment_id'])
    else:
        return False
