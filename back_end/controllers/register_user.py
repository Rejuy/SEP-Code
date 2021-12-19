# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services import register_user_service
from headers import *
from services.mysql_service import db


bp = Blueprint(
    'registerUser',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/register_user_info', methods=['POST', 'GET'])
def registerUserInfo():
    try:
        db.reconnectDatabase()
        user_info = request.get_json()
        print("18======")
        if user_info is None:
            return jsonify({'state': BAD_ARGUMENTS}), 400
        print("21======")
        state = register_user_service.checkUserInfo(user_info)
        print("23======")
        return jsonify({'state': state}), 200
    except KeyError:
        print("26======")
        return jsonify({'state': BAD_ARGUMENTS}), 400

