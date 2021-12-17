# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.user_service import updateProfilePicture, getProfilePicture, getUserInfo, getUserFavorite, getUserLike, getUserItems
from services.save_image_service import saveImage
from headers import *
from services.code_service import coder
from services.id_to_name_service import getNameByID
from services.code_service import coder

bp = Blueprint(
    'user',
    __name__,
    # template_folder='../templates'
)

# 激活用户
@bp.route('/api/v1.0/save_user_icon', methods=['POST'])
def save_user_icon():
    try:
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
        user_id = coder.decode(request.get_json()['mask'])
        print(user_id)
        filepath = getProfilePicture(user_id)
        return jsonify({'state': 0, 'path': filepath}), 200
    except KeyError:
        return jsonify({'state': 1}), 400

@bp.route('/api/v1.0/get_user_info', methods=['POST'])
def get_user_info():
    try:
        user_id = coder.decode(request.get_json()['mask'])
        user_info = getUserInfo(user_id)
        return jsonify({'state': 0, 'user': user_info}), 200
    except KeyError:
        return jsonify({'state': 1}), 400

# 获取用户收藏
@bp.route('/api/v1.0/get_user_favorites', methods=['POST'])
def get_user_favorites():
    try:
        user_id = coder.decode(request.get_json()['mask'])
        user_info = getUserFavorite(user_id)
        return jsonify({'state': 0, 'favorites': user_info}), 200
    except KeyError:
        return jsonify({'state': 1}), 400

# 获取用户点赞
@bp.route('/api/v1.0/get_user_likes', methods=['POST'])
def get_user_likes():
    try:
        user_id = coder.decode(request.get_json()['mask'])
        user_name = getNameByID(user_id)
        user_info = getUserLike(user_name)
        return jsonify({'state': 0, 'likes': user_info}), 200
    except KeyError:
        return jsonify({'state': 1}), 400

# 获取用户创作的推荐
@bp.route('/api/v1.0/get_user_items', methods=['POST'])
def get_user_items():
    try:
        info = request.get_json()
        user_id = coder.decode(info['mask'])
        user_items = getUserItems(user_id, info['class'])
        return jsonify({'state': 0, 'items': user_items}), 200
    except KeyError:
        return jsonify({'state': 1}), 400

