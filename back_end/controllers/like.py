# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.like_service import modifyUserLike
from headers import *
from services.code_service import coder
from services.id_to_name_service import getNameByID
from services.mysql_service import db


bp = Blueprint(
    'like',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/like', methods=['POST'])
def modifyLike():
    """
    :param raw_info:{
        mask:
        comment_id:
        operation: 1点赞，0删除点赞
    }
    :return: {
        state: 0成功,1失败
    }
    """
    try:
        db.reconnectDatabase()
        raw_info = request.get_json()
        id = coder.decode(raw_info['mask'])
        raw_info['user'] = getNameByID(id)
        if modifyUserLike(raw_info):
            return jsonify({'state': 0})
        else:
            return jsonify({'state': 1})
    except KeyError:
        return jsonify({"state": 1})