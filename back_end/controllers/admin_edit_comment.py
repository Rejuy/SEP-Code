# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.admin_service import *
from services.mysql_service import db


bp = Blueprint(
    'admin_edit_comment',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/admin_edit_comment', methods=['POST'])
def adminEditComment():
    try:
        db.reconnectDatabase()
        info = request.get_json()
        if info is None:
            return jsonify({'status': 1}), 400
        if not checkSecretCode(info['secret_code']):
            return jsonify({'status': 1}), 400
        if editComment(info):
            return jsonify({'status': 0}), 200
        return jsonify({'status': 1}), 200
    except KeyError:
        return jsonify({'status': 1}), 400

