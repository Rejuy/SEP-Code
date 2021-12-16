# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services import admin_service
from headers import *


bp = Blueprint(
    'user_count',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/admin_get_user_count', methods=['POST'])
def adminGetUserCount():
    try:
        user_info = request.get_json()
        if user_info is None:
            return jsonify({'status': 1, 'user_count': -1}), 400
        if not admin_service.checkSecretCode(user_info['secret_code']):
            return jsonify({'status': 1, 'user_count': -1}), 400
        user_count = admin_service.getUserCount()
        return jsonify({'status': 0, 'user_count': user_count}), 200
    except KeyError:
        return jsonify({'status': 1, 'user_count': -1}), 400

