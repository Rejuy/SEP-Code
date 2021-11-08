# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services import login_service
from headers import *


bp = Blueprint(
    'register',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/login', methods=['POST'])
def login():
    try:
        user_info = request.get_json()
        if user_info is None:
            return jsonify({'state': BAD_ARGUMENTS}), 400
        state = login_service.checkLoginInfo(user_info)
        return jsonify({'state': state}), 200
    except KeyError:
        return jsonify({'state': BAD_ARGUMENTS}), 400

