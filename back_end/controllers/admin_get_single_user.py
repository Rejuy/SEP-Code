# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.admin_service import *
from services.mysql_service import db


bp = Blueprint(
    'admin_get_single_user',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/admin_get_single_user', methods=['POST'])
def adminOperateItem():
    try:
        db.reconnectDatabase()
        info = request.get_json()
        if info is None:
            return jsonify({'status': 1}), 400
        if not checkSecretCode(info['secret_code']):
            return jsonify({'status': 1}), 400
        user = getSingleUser(info['id'])
        if user:
            return jsonify({'status': 0, "user": user}), 200
        return jsonify({'status': 1}), 200
    except KeyError:
        return jsonify({'status': 1}), 400

