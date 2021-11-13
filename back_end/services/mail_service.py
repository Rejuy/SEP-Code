from flask import Flask, request
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)
# 给flask配置文件添加配置信息
# 这个配置信息类似一个字典，可以追加数据
app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.163.com',
    MAIL_PORT=465,
    MAIL_USE_TLS = False, # SSL（Security Socket Layer,安全套接字层）和TLS（Transport Layer Sceurity，传输层安全）是两种常用的电子邮件安全协议
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'thu_rec@163.com',
    MAIL_PASSWORD = 'FURIFKYSUPBEVQGR', # 授权码而不是邮箱登录密码。
    SECRET_KEY = 'affdasfadar32323'
)

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email)

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token)
    except:
        return False
    return email

def activate_user(email):
    # TODO：
    # 将数据库中用户的激活状态改为成功
    pass

# 创建邮件对象工具
mail = Mail(app)

# 异步发送电子邮件
from threading import Thread
def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients) # # sender 发送方邮箱，recipients 接受方邮箱列表
    msg.body = text_body # 纯文本信息
    msg.html = html_body # HTML格式的信息
    Thread(target=send_async_email,args=(app,msg)).start()
    # send_async_email(app, msg)
 
# 发送验证邮件
def send_register_email(recipient):
    html_body = '<p>Welcome! Thanks for signing up. Please follow this link to activate your account:</p> \
<p><a href="{confirm_url}" target="_blank">{confirm_url}</a></p> \
<br> \
<p>Cheers!</p>'
    # 将要发送的链接嵌进去
    confirm_url = 'http://localhost:5001/'+'activate?code='+generate_confirmation_token(recipient)
    send_email('test subject',app.config['MAIL_USERNAME'],[recipient], 'text body', html_body = html_body.format(confirm_url = confirm_url))
 

@app.route('/activate', methods=['GET'])
def confirm_register():
    email = confirm_token(request.args.get('code'))
    print(email)
    return '验证成功'

@app.route('/email')
def index():
    # 这里是测试邮件功能，请把下面的邮箱改成你自己的邮箱
    test_email = '1241992824@qq.com'
    send_register_email(test_email)
    return '发送成功'
   

if __name__ == '__main__':
    app.run(port=5001, debug=True)