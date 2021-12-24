# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.random_list_service import *
from services.mysql_service import db


bp = Blueprint(
    'get_random_list',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/get_random_list', methods=['GET'])
def getRandomList():
    try:
        db.reconnectDatabase()
        print('afsd')
        result = randomList()
        return jsonify({"content": result}), 200
    except KeyError:
        return jsonify({'content': []}), 400

