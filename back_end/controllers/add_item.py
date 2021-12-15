# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.add_item_service import *


bp = Blueprint(
    'addItem',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/add_item', methods=['POST'])
def addItem():
    try:
        item_info = request.get_json()
        if item_info is None:
            return jsonify({'status': 0}), 400
        flag, user_id = checkUserExisted(item_info['mask'])
        if not flag:
            return jsonify({'status': 0}), 400
        if checkItemExisted(item_info):
            return jsonify({'status': 1}), 400
        if not userAddItem(item_info):
            return jsonify({'status': 0}), 400
        return jsonify({'status': 2}), 200
    except KeyError:
        return jsonify({'status': 0}), 400

