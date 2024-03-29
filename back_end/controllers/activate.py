# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services import mail_service
from headers import *
from services.mysql_service import db


bp = Blueprint(
    'activate',
    __name__,
    # template_folder='../templates'
)

# 激活用户
@bp.route('/api/v1.0/activate', methods=['GET'])
def activate_register():
    try:
        db.reconnectDatabase()
        email = mail_service.confirm_token(request.args.get('code'))
        mail_service.activate_user(email)
        return '验证成功', 200
    except KeyError:
        return '验证失败', 400

