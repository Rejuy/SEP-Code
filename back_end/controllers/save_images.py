# TODO
# 以后可能会用到
# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from services.save_image_service import saveImage
from headers import *
from io import BytesIO
import matplotlib.pyplot as plt
from services.mysql_service import db


bp = Blueprint(
    'savefile',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/save_images', methods=['POST'])
def save_images():
    try:
        db.reconnectDatabase()
        imageFileStorage = request.files['image']
        filepath = saveImage(imageFileStorage)
        return filepath
    except KeyError:
        return '保存失败', 400

