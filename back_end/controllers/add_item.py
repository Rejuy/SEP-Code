# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.add_item_service import *
from services.mysql_service import db


bp = Blueprint(
    'addItem',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/add_item', methods=['POST'])
def addItem():
    try:
        db.reconnectDatabase()
        item_info = request.get_json()
        # 判断info是否合法
        if item_info is None:
            return jsonify({'status': 0}), 400
        # 判断用户是否存在
        flag, user_id = checkUserExisted(item_info['mask'])
        if not flag:
            return jsonify({'status': 0}), 400
        # 判断item是否有同名存在
        """
        flag = checkItemExisted(item_info)
        if flag == "error":
            return jsonify({'status': 0}), 400
        elif flag:
            return jsonify({'status': 1}), 400
        """
        # 判断addItem是否成功
        flag = userAddItem(item_info, int(user_id))
        if flag == "error":
            return jsonify({'status': 0}), 400
        elif not flag:
            return jsonify({'status': 0}), 400
        return jsonify({'status': 2}), 200
    except KeyError:
        print(33)
        return jsonify({'status': 0}), 400

