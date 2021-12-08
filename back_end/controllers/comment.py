# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.comment_service import getCommentsByName
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
    "user": str,
    "text": str,
    "imageurls": list of str,
}
{
    "user": "zbw",
    "text": "good!",
    "imageurls": ["thurec.xyz/static/efaIZYWqFoyH3c3ee2488ab73f783cefd929f008c8fc.png"]
}
        """ 
        comment['image'] = json.dumps(comment['imageurls']) # 将url列表转换为字符串保存。
        db.addComment(comment) #TODO
        return '添加成功'

    except KeyError:
        return jsonify({'state': BAD_ARGUMENTS}), 400

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

