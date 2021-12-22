# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.course_service import getCourseItem
from headers import *
from services.mysql_service import db


bp = Blueprint(
    'course_item',
    __name__,
    # template_folder='../templates'
)

# 获取单个课程信息

@bp.route('/api/v1.0/get_course_item', methods=['POST'])
def courseItem():
    try:
        db.reconnectDatabase()
        info = request.get_json()
        if info is None:
            return jsonify({}), 400
        item, flag = getCourseItem(info)  # content_list为查询到的列表，flag为访问是否正确
        if not flag:
            return jsonify({}), 200
        return jsonify(item), 200
    except KeyError:
        return jsonify({}), 400

