# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.courses_list_service import getCoursesList
from headers import *


bp = Blueprint(
    'courses_list',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/get_courses_list', methods=['POST'])
def coursesList():
    try:
        print("Enter get_courses_list......")
        raw_info = request.get_json()
        if raw_info is None:
            return jsonify({'state': BAD_ARGUMENTS}), 400
        print("Request no problem")
        content_list, flag = getCoursesList(raw_info)  # content_list为查询到的列表，flag为访问是否正确
        print("Get content list")
        if not flag:
            return jsonify({'state': BAD_ARGUMENTS}), 200
        print("Content list no problem")
        return jsonify({'content_list': content_list}), 200
    except KeyError:
        return jsonify({'state': BAD_ARGUMENTS}), 400

