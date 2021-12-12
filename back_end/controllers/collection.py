# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.collection_service import modifyUserCollection
from headers import *
from services.code_service import coder

bp = Blueprint(
    'collection',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/collection', methods=['POST'])
def modifyCollection():
    """
    :param raw_info:{
        mask:
        class:
        item_id:
        operation: 1收藏，0取消收藏
    }
    :return: {
        state: 0成功,1失败
    }
    """
    try:
        raw_info = request.get_json()
        raw_info['user_id'] = coder.decode(raw_info['mask'])
        modifyUserCollection(raw_info)
        return jsonify({'state': 0})
    except KeyError:
        return jsonify({"state": 1})