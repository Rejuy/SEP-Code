# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.mail_service import send_feedback_email
from services import register_user_service
from headers import *


bp = Blueprint(
    'feedback',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/post_user_feedback', methods=['POST'])
def postUserFeedback():
    try:
        user_info = request.get_json()
        
        if user_info is None:
            return '反馈失败'

        send_feedback_email('hhhh', user_info['email'])
        
        return '反馈成功'

    except KeyError:
        print("26======")
        return jsonify({'state': BAD_ARGUMENTS}), 400

