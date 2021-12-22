# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from headers import start_date
from services.admin_service import *


bp = Blueprint(
    'admin_get_online_time',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/admin_get_online_time', methods=['POST'])
def adminOperateItem():
    try:
        info = request.get_json()
        if info is None:
            return jsonify({'status': 1}), 400
        if not checkSecretCode(info['secret_code']):
            return jsonify({'status': 1}), 400
        return jsonify({'status': 0, "date": start_date}), 200
    except KeyError:
        return jsonify({'status': 1}), 400

