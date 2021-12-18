# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.admin_service import *


bp = Blueprint(
    'item_list',
    __name__,
    # template_folder='../templates'
)


# 获取课程列表
@bp.route('/api/v1.0/admin_get_item_list', methods=['POST'])
def adminGetItems():
    try:
        raw_info = request.get_json()
        if raw_info is None:
            return jsonify({'status': 1, 'items': []}), 400
        if not checkSecretCode(raw_info['secret_code']):
            return jsonify({'status': 1, 'items': []}), 400
        item_list, flag = adminGetItemList(raw_info)
        if not flag:
            return jsonify({'status': 1, 'items': []}), 200
        return jsonify({'status': 0, 'items': item_list}), 200
    except KeyError:
        return jsonify({'status': 1, 'items': []}), 400

