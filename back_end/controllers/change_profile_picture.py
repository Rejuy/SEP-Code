# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services import change_profile_picture_service
from headers import *


bp = Blueprint(
    'change_profile_picture',
    __name__,
    # template_folder='../templates'
)

# 激活用户
@bp.route('/api/v1.0/change_profile_picture', methods=['POST'])
def change_profile_picture():
    try:
        user_info = request.get_json()
        change_profile_picture_service.updateProfilePicture(user_info['user_name'], user_info['pic_url'])
        return '更改成功', 200
    except KeyError:
        return '更改失败', 400

