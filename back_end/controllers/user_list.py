# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services import admin_service
from headers import *
from services.mysql_service import db


bp = Blueprint(
    'user_list',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/admin_get_users', methods=['POST'])
def adminGetUsers():
    try:
        db.reconnectDatabase()
        info = request.get_json()
        print("====enter get users====")
        if info is None:
            return jsonify({'status': 1, 'users': []}), 400
        print(21)
        if not admin_service.checkSecretCode(info['secret_code']):
            return jsonify({'status': 1, 'users': []}), 400
        print(24)
        user_list, flag = admin_service.getUserList(info)
        return jsonify({'status': 0, 'users': user_list}), 200
    except KeyError:
        print(28)
        return jsonify({'status': 1, 'users': []}), 400

