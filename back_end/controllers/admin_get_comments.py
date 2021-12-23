# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.admin_service import *
from services.mysql_service import db


bp = Blueprint(
    'admin_get_comments',
    __name__,
    # template_folder='../templates'
)


# 获取课程列表
@bp.route('/api/v1.0/admin_get_comments', methods=['POST'])
def adminGetItems():
    try:
        db.reconnectDatabase()
        raw_info = request.get_json()
        if raw_info is None:
            return jsonify({'status': 1}), 400
        if not checkSecretCode(raw_info['secret_code']):
            return jsonify({'status': 1}), 400
        comments_list, flag = db.getAllComments()
        if not flag:
            return jsonify({'status': 1}), 200
        return jsonify({'status': 0, 'comments': comments_list}), 200
    except KeyError:
        print(30)
        return jsonify({'status': 1, 'items': []}), 400

