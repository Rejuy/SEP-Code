# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.place_service import getPlaceItem
from headers import *


bp = Blueprint(
    'place_item',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/get_place_item', methods=['POST'])
def placeItem():
    try:
        info = request.get_json()
        if info is None:
            return jsonify({'item': {}}), 400
        item, flag = getPlaceItem(info['id'])  # content_list为查询到的列表，flag为访问是否正确
        if not flag:
            return jsonify({'item': {}}), 200
        return jsonify({'item': item}), 200
    except KeyError:
        return jsonify({'item': {}}), 400

