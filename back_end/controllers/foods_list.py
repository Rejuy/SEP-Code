# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.courses_list_service import getCoursesList
from headers import *


bp = Blueprint(
    'foods_list',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/get_foods_list', methods=['POST'])
def foodsList():
    try:
        print("Enter get_courses_list......")
        raw_info = request.get_json()
        if raw_info is None:
            return jsonify({'total_courses': -1, 'courses': None}), 400
        print("Request no problem")
        content_list, course_count, flag = getCoursesList(raw_info)  # content_list为查询到的列表，flag为访问是否正确
        print("Get content list")
        if not flag:
            return jsonify({'total_courses': -1, 'courses': None}), 200
        print("Content list no problem")
        return jsonify({'total_courses': course_count, 'courses': content_list}), 200
    except KeyError:
        return jsonify({'total_courses': -1, 'courses': None}), 400

