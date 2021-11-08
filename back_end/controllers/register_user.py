# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services import register_user_service
from headers import *


bp = Blueprint(
    'registerUser',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/register_user_info', methods=['POST', 'GET'])
def registerUserInfo():
    try:
        user_info = request.get_json()
        if user_info is None:
            return jsonify({'state': BAD_ARGUMENTS}), 400
        state = register_user_service.checkUserInfo(user_info)
        return jsonify({'state': state}), 200
    except KeyError:
        return jsonify({'state': BAD_ARGUMENTS}), 400

