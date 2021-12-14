from services.mysql_service import db
from services.login_service import admin_secret_code


def checkSecretCode(secret_code):
    if admin_secret_code != secret_code:
        return False
    return True


def getUserCount():
    return db.getTableCount("user")


def getUserList(info):
    """
    :param info: {
        "offset":,
        "size":
    }
    :return: list<user>
    """
    return db.getUserList(info)
