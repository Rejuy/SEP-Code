# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services import mail_service
from headers import *


bp = Blueprint(
    'activate',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/activate', methods=['GET'])
def activate_register():
    try:
        email = mail_service.confirm_token(request.args.get('code'))
        mail_service.activate_user(email)
        return '验证成功', 200
    except KeyError:
        return '验证失败', 400

