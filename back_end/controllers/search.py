# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services import search_service
from headers import *
from services.mysql_service import db


bp = Blueprint(
    'search',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/global_search', methods=['POST'])
def global_search():
    
    try:
        db.reconnectDatabase()
        info = request.get_json()
        item_list, count = search_service.globalSearch(info)
        return jsonify({'state': 0, 'items': item_list, "count": count})
    except KeyError:
        return jsonify({'state': -1})

@bp.route('/api/v1.0/limited_search', methods=['POST'])
def limited_search():
    
    try:
        db.reconnectDatabase()
        info = request.get_json()
        print(info)
        print(info)
        item_list = search_service.limitedSearch(info['class'], info['like'])
        return jsonify({'state': 0, 'items': item_list})
    except KeyError:
        return jsonify({'state': -1})