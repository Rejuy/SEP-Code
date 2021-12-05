import mysql.connector
from config.settings import *
import datetime
from headers import *


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
            check_email = (email,)
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
            check_user_name = (user_name,)
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

    def addComment(self, user_comment): #TODO
        try:
            sql = "INSERT INTO comment "
            sql += self.getKeysStr(INSERT_USER_KEY) + " VALUES " + self.producePlaceHolder(len(INSERT_USER_KEY))
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            comment = (
                user_comment['user_name'],
                user_comment['password'],
                user_comment['email'],
                time, 0, 0, 0, 0, 0
            )
            # 写入新数据
            self.cursor.execute(sql, comment)
            # 数据表内容更新
            self.connection.commit()
            return True
        except Exception as e:
            print("[Error] (addComment)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def delComment(self, key, val):
        # 不同方式删除用户（指定键值）
        try:
            # 删除数据
            sql = "DELETE FROM comment WHERE " + key + " = %s"
            del_val = (val,)
            self.cursor.execute(sql, del_val)
            # 数据表内容更新
            self.connection.commit()
            return True
        except Exception as e:
            print("[Error] (delComment)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def addUser(self, user_info):
        try:
            sql = "INSERT INTO user "
            sql += self.getKeysStr(INSERT_USER_KEY) + " VALUES " + self.producePlaceHolder(len(INSERT_USER_KEY))
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
            del_val = (val,)
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
            get_val = (val,)
            self.cursor.execute(sql, get_val)
            user = self.cursor.fetchone()
            return user
        except Exception as e:
            print("[Error] (getUser)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return None

    def updateData(self, table, locate_key, locate_value, update_key, update_value):
        try:
            # 更新数据
            sql = "UPDATE " + table + " SET " + update_key + " = %s WHERE " + locate_key + " = %s"
            val = (update_value, locate_value)
            self.cursor.execute(sql, val)
            self.connection.commit()
            return True
        except Exception as e:
            print("[Error] (updateData)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def addContent(self, table, content_info):
        try:
            sql = "INSERT INTO " + table + " ("
            key_list, val = [], ()
            if (table == "couse_list"):
                keylist = INSERT_COURSES_KEY
            sql += self.getKeysStr(key_list) + ") VALUES " + self.producePlaceHolder(len(key_list))
            for key in key_list:
                try:
                    val += (content_info[key], )
                except:
                    val += (0, )
            # 写入新数据
            self.cursor.execute(sql, val)
            # 数据表内容更新
            self.connection.commit()
            return True
        except Exception as e:
            print("[Error] (addContent)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def getContentList(self, table, info):
        '''
        :param info: {
            key_list: (list)
            filter: (str)
            sort_order: (str)
            sort_criteria: (str)
            index_begin:
            content_count:
        }
        :return: list
        '''
        try:
            # 获得数据
            sql = "SELECT " + self.getKeysStr(info['key_list']) + " FROM " + table
            val = ()
            # 判断是否需要筛选，若是则加上筛选部分sql语句
            if info['filter'] != '':
                sql += " WHERE " + info['filter'] + " = %s "
                val += (info['filter_value'], )
            # 判断是否需要排序，若是则加上排序部分sql语句
            if info['sort_order'] != "not_sort":
                sql += " order by " + info['sort_criteria'] + " "
                if info['sort_order'] == 'desc':
                    sql += 'desc '
            # 进行分页操作
            sql += " LIMIT " + str(info['content_count']) + " OFFSET " + str(info['index_begin'])
            self.cursor.execute(sql, val)
            content_list = self.cursor.fetchall()
            return content_list, True
        except Exception as e:
            print("[Error] (getContentList)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return None, False

    def tupleToDict(self, tuple, key_list):
        # 将元组转化为字典
        dict = {}
        for i in range(len(key_list)):
            dict[key_list[i]] = tuple[i]
        return dict

    def getKeysStr(self, key_list):
        if len(key_list) == 0:
            return ''
        string = key_list[0]
        for i in range(1, len(key_list)):
            string += ", " + key_list[i]
        return string

    def producePlaceHolder(self, count):
        place_holder = "(%s"
        for i in range(count - 1):
            place_holder += ", %s"
        place_holder += ")"
        return place_holder

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
