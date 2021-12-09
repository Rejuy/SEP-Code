from werkzeug.datastructures import FileStorage
from os import path

def saveImage (imageFileStorage):
    filepath = path.join('static', imageFileStorage.filename)
    imageFileStorage.save(filepath)
    return filepath