# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services import admin_service
from headers import *


bp = Blueprint(
    'user_list',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/admin_get_users', methods=['POST'])
def adminGetUsers():
    try:
        info = request.get_json()
        if info is None:
            return jsonify({'status': 1, 'users': []}), 400
        if not admin_service.checkSecretCode(info['secret_code']):
            return jsonify({'status': 1, 'users': []}), 400
        user_list, flag = admin_service.getUserList(info)
        return jsonify({'status': 0, 'users': user_list}), 200
    except KeyError:
        return jsonify({'status': 1, 'users': []}), 400

