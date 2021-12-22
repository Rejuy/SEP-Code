# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.course_service import *
from services.mysql_service import db


bp = Blueprint(
    'view_full_content',
    __name__,
    # template_folder='../templates'
)

# 激活用户
@bp.route('/api/v1.0/view_full_content', methods=['POST'])
def viewFullContent():
    try:
        db.reconnectDatabase()
        info = request.get_json()
        result, flag = getFullContent(info['id'])
        return jsonify(result), 200
    except KeyError:
        return jsonify({}), 400


