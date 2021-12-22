# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.admin_service import *
from services.mysql_service import db


bp = Blueprint(
    'admin_get_single_comment',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/admin_get_single_comment', methods=['POST'])
def adminOperateItem():
    try:
        db.reconnectDatabase()
        info = request.get_json()
        if info is None:
            return jsonify({'status': 1}), 400
        if not checkSecretCode(info['secret_code']):
            return jsonify({'status': 1}), 400
        comment, flag = db.getData("comment", ["id"], [info['id']], ADMIN_COMMENT_KEY)
        comment[0]['user_id'] = db.getData("user", ["user_name"], [comment[0]["user"]], ["id"], get_all=False)[0]['id']
        if flag:
            return jsonify({'status': 0, "comment": comment[0]}), 200
        return jsonify({'status': 1}), 200
    except KeyError:
        return jsonify({'status': 1}), 400

