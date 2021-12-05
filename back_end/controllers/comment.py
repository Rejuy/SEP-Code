# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.mail_service import send_feedback_email
from services.mysql_service import db
from headers import *
import json

bp = Blueprint(
    'comment',
    __name__,
    # template_folder='../templates'
)


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
        return '评论成功'

    except KeyError:
        return jsonify({'state': BAD_ARGUMENTS}), 400

@bp.route('/api/v1.0/get_comment', methods=['POST'])
def getComment():
    try:
        id = request.get_json()["id"]
        # print(id)
        commentList = db.getComment(id) #TODO
        # commentList = [{"id": 5, "user": "zbw"}, {"id": 5, "user": "zxl"}]
        return jsonify(commentList)

    except KeyError:
        return jsonify({'state': BAD_ARGUMENTS}), 400

