# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.food_service import getFoodItem
from headers import *
from services.mysql_service import db


bp = Blueprint(
    'food_item',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/get_food_item', methods=['POST'])
def foodItem():
    try:
        db.reconnectDatabase()
        info = request.get_json()
        if info is None:
            return jsonify({'item': {}}), 400
        item, flag = getFoodItem(info['id'])  # content_list为查询到的列表，flag为访问是否正确
        if not flag:
            return jsonify({'item': {}}), 200
        return jsonify({'item': item}), 200
    except KeyError:
        return jsonify({'item': {}}), 400

