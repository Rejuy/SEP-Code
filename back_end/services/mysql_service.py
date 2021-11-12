import mysql.connector
from config.settings import *
import datetime


class MySQLDb:
    def __init__(self, host, user, password, database):
        # 建立数据库连接
        self.connection = mysql.connector.connect(
            host=host,
            # port=port,
            user=user,
            passwd=password,
            database=database
        )
        # 通过 cursor() 创建游标对象
        self.cursor = self.connection.cursor()

    def checkUserExistence(self, email):
        try:
            sql = "SELECT * FROM user WHERE email = %s"
            check_email = (email, )
            # 使用 execute() 查询 email
            self.cursor.execute(sql, check_email)
            result = self.cursor.fetchall()
            if len(result) == 0:
                return False
            else:
                return True
        except Exception as e:
            print("[Error] (checkUserExistence)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def checkUserNameExistence(self, user_name):
        try:
            sql = "SELECT * FROM user WHERE user_name = %s"
            check_user_name = (user_name, )
            # 使用 execute() 查询 user_name
            self.cursor.execute(sql, check_user_name)
            result = self.cursor.fetchall()
            if len(result) == 0:
                return False
            else:
                return True
        except Exception as e:
            print("[Error] (checkUserNameExistence)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def addUser(self, user_info):
        try:
            sql = "INSERT INTO user (user_name, password, email, account_birth, collection_count, like_count, comment_count, content_count, activated) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user = (
                user_info['user_name'],
                user_info['password'],
                user_info['email'],
                time, 0, 0, 0, 0, 0
            )
            # 写入新数据
            self.cursor.execute(sql, user)
            # 数据表内容更新
            self.connection.commit()
            return True
        except Exception as e:
            print("[Error] (addUser)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def delUser(self, key, val):
        # 不同方式删除用户（指定键值）
        try:
            # 删除数据
            sql = "DELETE FROM user WHERE " + key + " = %s"
            del_val = (val, )
            self.cursor.execute(sql, del_val)
            # 数据表内容更新
            self.connection.commit()
            return True
        except Exception as e:
            print("[Error] (delUser)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def getUser(self, key, val):
        # 用于用户登录成功后返回给前端用户的基本信息，返回格式为字典
        # TODO
        #  考虑图片的前后端传输？
        try:
            # 获得数据
            sql = "SELECT * FROM user WHERE " + key + " = %s"
            get_val = (val, )
            self.cursor.execute(sql, get_val)
            user = self.cursor.fetchone()
            return user
        except Exception as e:
            print("[Error] (getUser)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return None

    def select_db(self, sql):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        # 使用 execute() 执行sql
        self.cur.execute(sql)
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        return data

    def execute_db(self, sql):
        """更新/新增/删除"""
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.connection.ping(reconnect=True)
            # 使用 execute() 执行sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print("操作出现错误：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()

'''
    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cursor.close()
        # 关闭数据库连接
        self.connection.close()
'''


db = MySQLDb(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)

