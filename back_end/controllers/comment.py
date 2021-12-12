# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.comment_service import getCommentsByName, getCommentsByItem, getCommentsByComment
from services.mysql_service import db
from services.id_to_name_service import getNameByID
from headers import *
from services.code_service import coder
import json

bp = Blueprint(
    'comment',
    __name__,
    # template_folder='../templates'
)

# 添加评论
@bp.route('/api/v1.0/add_comment', methods=['POST'])
def addComment():
    try:
        comment = request.get_json()
        """
comment = {
    "class": str, class=1课程,class=2饮食,class=3出行
    "item_id"： 推荐的物品在表中对应的id
    "user": str,
    "star": str,
    "text": str,
    "imageurls": list of urls(str),
    "upper_comment_id": 如果是对推荐的评论：那么这里是推荐的id，否则为-1
}

{
    "class": 1,
    "item_id": 1,
    "user": "zhangbw",
    "star": 4,
    "text": "good!",
    "imageurls": ["thurec.xyz/static/efaIZYWqFoyH3c3ee2488ab73f783cefd929f008c8fc.png"],
    "upper_comment_id": -1
}
        """ 
        comment['image'] = json.dumps(comment['imageurls']) # 将url列表转换为字符串保存。

        table_name = ["hhh", "course_list", "food_list", "place_list"]
        comment['table'] = table_name[comment['class']]

        db.addComment(comment) #TODO
        return jsonify({'state': 1})

    except KeyError:
        return jsonify({'state': -1}), 400

# 获取用户历史评论
@bp.route('/api/v1.0/get_comment_by_id', methods=['POST'])
def get_comment_by_id():
    try:
        info = request.get_json()
        id = coder.decode(info['mask'])
        # print(id)
        user_name = getNameByID(id)
        # print(user_name)
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