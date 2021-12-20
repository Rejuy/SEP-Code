# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.admin_service import *
from services.mysql_service import db


bp = Blueprint(
    'admin_operate_item',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/admin_operate_item', methods=['POST'])
def adminOperateItem():
    try:
        db.reconnectDatabase()
        info = request.get_json()
        if info is None:
            return jsonify({'status': 1, 'flag': -1}), 400
        if not checkSecretCode(info['secret_code']):
            return jsonify({'status': 1, 'flag': -1}), 400
        flag = operateItem(info)
        return jsonify({'status': 0, 'flag': flag}), 200
    except KeyError:
        return jsonify({'status': 1, 'flag': -1}), 400

