# TODO
# 以后可能会用到
# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services import mail_service
from headers import *


bp = Blueprint(
    'viewfile',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/viewfile', methods=['GET'])
def activate_register():
    try:
        target_url = request.args.get('f')
        return '验证成功', 200
    except KeyError:
        return '验证失败', 400

