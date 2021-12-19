# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services import login_service
from services.mysql_service import db


bp = Blueprint(
    'admin_login',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/admin_login', methods=['POST'])
def adminLogin():
    try:
        db.reconnectDatabase()
        user_info = request.get_json()
        if user_info is None:
            return jsonify({'status': 1, 'secret_code': ""}), 400
        status, mask = login_service.checkAdminLoginInfo(user_info)  # user为当前用户的基本信息，格式为字典
        return jsonify({'status': status, 'secret_code': "X/hRrvQGaJ3HYVebsklp1TxRAjl6qQ2NR99wa/chOqE="}), 200
    except KeyError:
        return jsonify({'status': 1, 'secret_code': ""}), 400

