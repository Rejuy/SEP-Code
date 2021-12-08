# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.course_service import getCourseItem
from headers import *


bp = Blueprint(
    'course_item',
    __name__,
    # template_folder='../templates'
)

# 获取单个课程信息

@bp.route('/api/v1.0/get_course_item', methods=['POST'])
def courseItem():
    try:
        info = request.get_json()
        if info is None:
            return jsonify({'item': None}), 400
        item, flag = getCourseItem(info['id'])  # content_list为查询到的列表，flag为访问是否正确
        if not flag:
            return jsonify({'item': None}), 200
        return jsonify({'item': item}), 200
    except KeyError:
        return jsonify({'item'}), 400

