# TODO
# 以后可能会用到
# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from werkzeug.datastructures import FileStorage
from services import mail_service
from headers import *
from io import BytesIO
from os import path
import matplotlib.pyplot as plt

bp = Blueprint(
    'savefile',
    __name__,
    # template_folder='../templates'
)


@bp.route('/api/v1.0/save_images', methods=['POST'])
def save_images():
    try:
        # print('19')
        # print(request.form)
        # print('21')
        # print(request.files)
        imageFileStorage = request.files['image']
        # print(imageFileStorage.filename)
        filepath = path.join('static', imageFileStorage.filename)
        imageFileStorage.save(filepath)
        # image_stream = request.files['user_feedback_image'].stream
        # image = image_stream.read()
        # print(path.dirname(app.instance_path))
        # print(type(request.files['user_feedback_image']))
        # plt.imshow(plt.imread(BytesIO(image)))
        # plt.show()
        return filepath
        return 'static/'+imageFileStorage.filename
    except KeyError:
        return '保存失败', 400

