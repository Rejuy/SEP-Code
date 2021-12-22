# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.admin_service import *
from services.mysql_service import db


bp = Blueprint(
    'admin_new_user_count',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/admin_new_user_count', methods=['POST'])
def adminOperateItem():
    try:
        db.reconnectDatabase()
        info = request.get_json()
        if info is None:
            return jsonify({'status': 1}), 400
        if not checkSecretCode(info['secret_code']):
            return jsonify({'status': 1}), 400
        count_list, flag = db.getNewUserCount(info['months'])
        if flag:
            return jsonify({'status': 0, 'count': count_list}), 200
        return jsonify({'status': 1}), 200
    except KeyError:
        return jsonify({'status': 1}), 400

