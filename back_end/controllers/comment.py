# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.mail_service import send_feedback_email
from services.mysql_service import db
from headers import *

bp = Blueprint(
    'comment',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/add_comment', methods=['POST'])
def addComment():
    try:

        comment = request.get_json()
        """
        comment = {
            'text': str,
            'star': int,
            'imageurls': list of str,
            'time': date_time
        }
        """
        print('gg')
        db.addContent('comment ', comment)
        return '评论成功'       

    except KeyError:
        print("26======")
        return jsonify({'state': BAD_ARGUMENTS}), 400

@bp.route('/api/v1.0/get_comment', methods=['POST', 'GET'])
def getComment():
    try:

        # user_info = request.get_json()
        # print(user_info)
        # user_text = user_info['user_text']
        # images_url = user_info['text']
        # user_info['star']
        print('gg')
        # send_feedback_email(user_info['user_text'], user_info['email'])
        
        return '获取评论'

    except KeyError:
        print("26======")
        return jsonify({'state': BAD_ARGUMENTS}), 400

