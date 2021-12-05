# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.mail_service import send_feedback_email
from services import register_user_service
from headers import *
from io import BytesIO
import matplotlib.pyplot as plt

bp = Blueprint(
    'add_comment',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/add_comment', methods=['POST'])
def postUserFeedback():
    try:
        user_info = request.get_json()
        # print(user_info)
        user_text = user_info['user_text']
        images_url = user_info['images_url']
        for image_url in images_url:
            user_text += "<p> <img src=\"https://" + image_url + "\"</p>"
        send_feedback_email(user_text, '1241992824@qq.com')
        # send_feedback_email(user_info['user_text'], user_info['email'])
        
        return '反馈成功'

    except KeyError:
        print("26======")
        return jsonify({'state': BAD_ARGUMENTS}), 400

