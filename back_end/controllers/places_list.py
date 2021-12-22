# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.place_service import getPlacesList
from headers import *
from services.mysql_service import db


bp = Blueprint(
    'places_list',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/get_places_list', methods=['POST'])
def placesList():
    try:
        db.reconnectDatabase()
        print("Enter get_places_list......")
        raw_info = request.get_json()
        if raw_info is None:
            return jsonify({'total_places': -1, 'places': []}), 400
        print("Request no problem")
        content_list, place_count, flag = getPlacesList(raw_info)  # content_list为查询到的列表，flag为访问是否正确
        print("Get content list")
        if not flag:
            return jsonify({'total_places': -1, 'places': []}), 200
        print("Content list no problem")
        return jsonify({'total_places': place_count, 'places': content_list}), 200
    except KeyError:
        return jsonify({'total_places': -1, 'places': []}), 400

