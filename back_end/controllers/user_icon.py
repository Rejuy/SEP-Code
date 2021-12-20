# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.user_icon_service import updateProfilePicture
from services.save_image_service import saveImage
from headers import *
from services.code_service import coder
from services.mysql_service import db


bp = Blueprint(
    'user_icon',
    __name__,
    # template_folder='../templates'
)

# 激活用户
@bp.route('/api/v1.0/save_user_icon', methods=['POST'])
def save_user_icon():
    try:
        db.reconnectDatabase()
        user_id = coder.decode(request.form['mask'])
        imageFileStorage = request.files['image']
        filepath = saveImage(imageFileStorage)
        updateProfilePicture(user_id, filepath)
        return jsonify({'state': 0, 'path': filepath}), 200
    except KeyError:
        return jsonify({'state': 1}), 400

@bp.route('/api/v1.0/get_user_icon', methods=['POST'])
def get_user_icon():
    try:
        db.reconnectDatabase()
        user_id = coder.decode(request.json()['mask'])
        GetProfilePicture(user_id, filepath)
        return jsonify({'state': 0, 'path': filepath}), 200
    except KeyError:
        return jsonify({'state': 1}), 400

