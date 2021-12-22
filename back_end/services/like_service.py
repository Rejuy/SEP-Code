from headers import *
from services.mysql_service import db


def modifyUserLike(raw_info):
    """
    :param raw_info:{
        user:
        comment_id:
    }
    :return: bool
    """
    liked = db.checkCommentLiked(raw_info['user'], raw_info['comment_id'])
    if not liked:
        return db.addLike(raw_info['user'], raw_info['comment_id']), liked
    else:
        return db.delLike(raw_info['user'], raw_info['comment_id']), liked
