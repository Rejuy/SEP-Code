from services import register_user_service

def EmailSendTest():
    standard_user_info = {
        'user_name': 'normal',
        'password': 'Ad000000$',
        'email': '1241992824@qq.com'
    }
    content = standard_user_info.copy()
    dd = register_user_service.checkUserInfo(content)
    print(dd)

if __name__ == '__main__':
    EmailSendTest()