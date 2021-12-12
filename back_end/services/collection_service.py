from headers import *
from services.mysql_service import db


def modifyUserCollection(raw_info):
    """
    :param raw_info:{
        user:
        comment_id:
        operation: 1点赞，0删除点赞
    }
    :return: bool

    example:

    {
        "mask": "0VNE4RlqHjkjQS6b9kGTfw==",
        "class": 1,
        "item_id": 1,
        "operation": 1
    }
    """
    collected = db.checkItemCollected(raw_info['class'], raw_info['item_id'], raw_info['user_id'])
    print('hh')
    if raw_info['operation'] == 1:
        if collected:
            return False
        db.addCollection(raw_info['class'], raw_info['item_id'], raw_info['user_id'])
    elif raw_info['operation'] == 0:
        if not collected:
            return False
        db.delCollection(raw_info['class'], raw_info['item_id'], raw_info['user_id'])
    else:
        return False
