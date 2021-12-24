# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.comment_service import getCommentsByName, getCommentsByItem, getCommentsByComment
from services.mysql_service import db
from services.id_to_name_service import getNameByID
from headers import *
from services.code_service import coder
import json
from services.mysql_service import db


bp = Blueprint(
    'comment',
    __name__,
    # template_folder='../templates'
)

# 添加评论
@bp.route('/api/v1.0/post_new_comment', methods=['POST'])
def addComment():
    try:
        db.reconnectDatabase()
        comment = request.get_json()
        if len(comment['user_text']) == 0:
            return jsonify({'state': 0}), 400
        id = coder.decode(comment['mask'])
        comment['user'] = getNameByID(id)
        comment['text'] = comment['user_text']
        del comment['user_text']
        comment['item_id'] = comment['id']
        del comment['id']
        comment['table'] = INT_TO_TABLE[comment['class']]
        db.addComment(comment)  # TODO
        return jsonify({'state': 1})

    except KeyError:
        return jsonify({'state': 0}), 400

# 获取用户历史评论
@bp.route('/api/v1.0/get_comment_by_id', methods=['POST'])
def get_comment_by_id():
    try:
        info = request.get_json()
        print(info)
        id = coder.decode(info['mask'])
        # print(id)
        user_name = getNameByID(id)
        comments = getCommentsByName(user_name, info['offset'], info['size']) #TODO
        # commentList = [{"id": 5, "user": "zbw"}, {"id": 5, "user": "zxl"}]
        return jsonify({'state': int(info['size'] != len(comments)), 'comments': comments})

    except KeyError:
        return jsonify({'state': 2}), 400

# 获取一个item的推荐列表(其中upper_comment_id=-1)
# 获取用户历史评论
@bp.route('/api/v1.0/get_comment_by_item', methods=['POST'])
def get_comment_by_item():
    '''
    post: {
        class:
        item_id:
    }
    return: {
        state: 成功0， 错误1
        comments: [
           {"user": ... ,"star": ..., "text": ...,"image": ...}, ...
        ]
    }
    example:
    post: {
        "class": 1,
        "item_id": 1
    }
    '''
    try:
        info = request.get_json()
        # print(user_name)
        comments = getCommentsByItem(info['class'], info['item_id']) #TODO
        # commentList = [{"id": 5, "user": "zbw"}, {"id": 5, "user": "zxl"}]
        return jsonify({'state': 0, 'comments': comments})

    except KeyError:
        return jsonify({'state': 1})

# 查看一个推荐下的所有评论
@bp.route('/api/v1.0/get_comment_for_comment', methods=['POST'])
def get_comment_for_comment():
    '''
    post: {
        comment_id:
    }
    return: {
        state: 成功0， 错误1
        comments: [
           {"user": ... ,"text": ...,"image": ...,"time": ..., "likes": ....}, ...
        ]
    }
    example:
    post: {
        "comment_id": 0
    }
    '''
    try:
        info = request.get_json()
        # print(user_name)
        comments = getCommentsByComment(info['comment_id']) #TODO
        # commentList = [{"id": 5, "user": "zbw"}, {"id": 5, "user": "zxl"}]
        return jsonify({'state': 0, 'comments': comments})

    except KeyError:
        return jsonify({'state': 1})