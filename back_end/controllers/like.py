# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.courses_list_service import getCoursesList
from headers import *


bp = Blueprint(
    'like',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/like', methods=['POST'])
def modifyLike():
    try:
        raw_info = request.get_json()
        if raw_info is None:
            return jsonify({"likes": -1}), 400
        print("Request no problem")
        content_list, course_count, flag = getCoursesList(raw_info)  # content_list为查询到的列表，flag为访问是否正确
        print("Get content list")
        if not flag:
            return jsonify({"likes": -1}), 200
        print("Content list no problem")
        return jsonify({'total_courses': course_count, 'courses': content_list}), 200
    except KeyError:
        return jsonify({"likes": -1}), 400

