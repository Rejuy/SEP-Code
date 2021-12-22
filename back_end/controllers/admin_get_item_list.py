# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.admin_service import *
from services.mysql_service import db


bp = Blueprint(
    'item_list',
    __name__,
    # template_folder='../templates'
)


# 获取课程列表
@bp.route('/api/v1.0/admin_get_item_list', methods=['POST'])
def adminGetItems():
    try:
        db.reconnectDatabase()
        raw_info = request.get_json()
        print(18)
        if raw_info is None:
            return jsonify({'status': 1, 'items': []}), 400
        print(21)
        if not checkSecretCode(raw_info['secret_code']):
            return jsonify({'status': 1, 'items': []}), 400
        print(24)
        print(raw_info)
        item_list, flag = adminGetItemList(raw_info)
        if not flag:
            return jsonify({'status': 1, 'items': []}), 200
        print(28)
        return jsonify({'status': 0, 'items': item_list}), 200
    except KeyError:
        print(30)
        return jsonify({'status': 1, 'items': []}), 400

