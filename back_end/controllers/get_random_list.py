# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.food_service import getFoodsList
from headers import *
from services.mysql_service import db


bp = Blueprint(
    'get_random_list',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/get_random_list', methods=['GET'])
def foodsList():
    try:
        db.reconnectDatabase()
        print("Enter get_foods_list......")
        if raw_info is None:
            return jsonify({'total_food': -1, 'food': []}), 400
        print("Request no problem")
        content_list, food_count, flag = getFoodsList(raw_info)  # content_list为查询到的列表，flag为访问是否正确
        print("Get content list")
        if not flag:
            return jsonify({'total_food': -1, 'food': []}), 200
        print("Content list no problem")
        return jsonify({'total_food': food_count, 'food': content_list}), 200
    except KeyError:
        return jsonify({'total_food': -1, 'foods': []}), 400

