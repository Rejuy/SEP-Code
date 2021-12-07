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

    def addItem(self, table, content_info):
        try:
            sql = "INSERT INTO " + table + " ("
            key_list, val = [], ()

            if table == "course_list":
                key_list = INSERT_COURSES_KEY
            elif table == "food_list":
                key_list = INSERT_FOOD_KEY
            elif table == "place_list":
                key_list = INSERT_PLACE_KEY

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
            # 更新class表的count值
            sql = "UPDATE class SET count = count + 1 WHERE name = %s"
            class_name = table.split("_")[0][0].upper() + table.split("_")[0][1:]
            val = (class_name, )
            self.cursor.execute(sql, val)
            # 数据表内容更新
            self.connection.commit()
            return True
        except Exception as e:
            print("[Error] (addContent)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def getItemList(self, table, info):
        '''
        :param info: {
            key_list: (list)
            filter:[
                {
                key: ...,
                value: ...
                }
            ]
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
            if len(info['filter']) != 0:
                sql += " WHERE " + info['filter'][0]['key'] + " = %s "
                val += (info['filter'][0]['value'], )
                if len(info['filter']) > 1:
                    for i in range(1, len(info['filter'])):
                        sql += " and " + info['filter'][i]['key'] + " = %s "
                        val += (info['filter'][i]['value'], )
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

    def getTableCount(self, table):
        try:
            sql = "SELECT COUNT(*) FROM " + table
            # 执行语句
            self.cursor.execute(sql)
            # 获得返回值
            count = self.cursor.fetchall()[0][0]
            return count
        except Exception as e:
            print("[Error] (getTableCount)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return -1

    def getItem(self, table, table_id, id, key_list):
        """
        recommendation: {
    	    user: ...;  # 用户
    	    star: ...;  # 评分 [0.0 - 5.0] 允许 .5
     	    time: ...;  # 发布时间
    	    likes: ....; # 点赞数量
    	    text: ....; # 评论内容
    	    image: ....; # 评论图片 (str)
    	    comment_numbers: ...;
	    }
        """
        try:
            # 获得数据
            sql = "SELECT " + self.getKeysStr(key_list) + " FROM " + table + " WHERE id = %s"
            val = (id, )
            self.cursor.execute(sql, val)
            raw_item = self.cursor.fetchone()
            # 转成字典
            item = self.tupleToDict(raw_item, key_list)
            # 获得相应评论
            sql = "SELECT * FROM comment WHERE class = %s AND item_id = %s"
            val = (table_id, id)
            self.cursor.execute(sql, val)
            comments_list = self.cursor.fetchall()
            for i in range(len(comments_list)):
                comments_list[i] = self.tupleToDict(comments_list[i], BASIC_ITEM_COMMENT_KEY)
                del comments_list[i]['id']
                comments_list[i]['time'] = comments_list[i]['time'].strftime("%Y-%m-%d %H:%M:%S")
                comments_list[i]['comment_numbers'] = comments_list[i]['lower_comment_count']
                del comments_list[i]['lower_comment_count']
            item['recommendations'] = comments_list
            return item, True
        except Exception as e:
            print("[Error] (getItem)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return None, False

    def addComment(self, comment_info):
        """
        进入之前要判断对应的item_id, user, upper_comment_id是否合理
        :param comment_info:{
            "class":,
            "table":,(class对应的表名)
            "item_id":,
            "user":,
            "upper_comment_id":,
            "star":,
            "text":,
            "image":
        }
        :return:
        """
        try:
            sql = "INSERT INTO comment ("
            val = ()
            sql += self.getKeysStr(INSERT_COMMENT_KEY) + ") VALUES " + self.producePlaceHolder(len(INSERT_COMMENT_KEY))
            for key in INSERT_COMMENT_KEY:
                try:
                    val += (comment_info[key], )
                except:
                    if key == "time":
                        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        val += (time, )
                    else:
                        val += (0, )
            # 写入新数据
            self.cursor.execute(sql, val)
            # 数据表内容更新
            self.connection.commit()
            # 更新其他表相应的值
            sql = "UPDATE " + comment_info['table'] + " SET score = (score * comment_count + 2 * %s) / (comment_count + 1), comment_count = comment_count + 1 WHERE id = %s"
            val = (comment_info['star'], comment_info['item_id'])
            self.cursor.execute(sql, val)  # 补上heat的更新
            self.connection.commit()

            sql = "SELECT score FROM " + comment_info['table'] + " WHERE id = %s"
            val = (comment_info['item_id'], )
            self.cursor.execute(sql, val)
            score = self.cursor.fetchone()[0]
            if score - int(score) >= 0.5:
                score = int(score) + 1
            else:
                score = int(score)
            star = score / 2
            sql = "UPDATE " + comment_info['table'] + " SET star = %s WHERE id = %s"
            val = (star, comment_info['item_id'])
            self.cursor.execute(sql, val)

            sql = "UPDATE user SET comment_count = comment_count + 1 WHERE user_name = %s"
            val = (comment_info['user'],)
            self.cursor.execute(sql, val)

            if comment_info['upper_comment_id'] != 0:
                sql = "UPDATE comment SET lower_comment_count = lower_comment_count + 1 WHERE id = %s"
                val = (comment_info['upper_comment_id'],)
                self.cursor.execute(sql, val)
            # 数据表内容更新
            self.connection.commit()
            return True
        except Exception as e:
            print("[Error] (addComment)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def addLike(self, user, comment_id):
        """
        :param comment_class: 评论所属的模块, 1,2,3
        :param user: 用户名
        :param comment_id: 评论的id
        :return:
        """
        try:
            sql = "INSERT INTO user_like ("
            sql += self.getKeysStr(INSERT_LIKE_KEY) + ") VALUES " + self.producePlaceHolder(len(INSERT_LIKE_KEY))
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            val = (user, comment_id, time)
            # 写入新数据
            self.cursor.execute(sql, val)
            # 数据表内容更新
            self.connection.commit()
            # 更新其他表相应的值
            sql = "UPDATE comment SET likes = likes + 1 WHERE id = %s"
            val = (comment_id, )
            self.cursor.execute(sql, val)

            sql = "UPDATE user SET like_count = like_count + 1 WHERE user_name = %s"
            val = (user, )
            self.cursor.execute(sql, val)

            # 数据表内容更新
            self.connection.commit()
            return True
        except Exception as e:
            print("[Error] (addLike)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def delLike(self, user, comment_id):
        """
        删除点赞
        :param user: 用户名
        :param comment_id: 评论id
        :return: bool
        """
        try:
            # 删除数据
            sql = "DELETE FROM user_like WHERE comment_id = %s AND user = %s"
            val = (comment_id, user)
            self.cursor.execute(sql, val)
            # 数据表内容更新
            self.connection.commit()
            return True
        except Exception as e:
            print("[Error] (delLike)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def checkCommentLiked(self, user, comment_id):
        """
        检查用户是否点赞过某个评论
        :param user: 用户名
        :return: bool
        """
        try:
            # 获得相应评论
            sql = "SELECT * FROM user_like WHERE user = %s AND comment_id = %s"
            val = (user, comment_id)
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                return True
            return False
        except Exception as e:
            print("[Error] (checkCommentLiked)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def getUserCommentList(self, user):
        """
        获得用户所有的评论
        :param user: 用户名
        :return: comment列表[{
            user:,
            star:,
            time:,
            likes:,
            text:,
            image:,
            class:,
            item_id:
        }]
        """
        try:
            # 获得相应评论
            sql = "SELECT * FROM comment WHERE user = %s"
            val = (user, )
            self.cursor.execute(sql, val)
            comments_list = self.cursor.fetchall()
            for i in range(len(comments_list)):
                comments_list[i] = self.tupleToDict(comments_list[i], COMMENT_KEY)
                del comments_list[i]['id']
                comments_list[i]['time'] = comments_list[i]['time'].strftime("%Y-%m-%d %H:%M:%S")
                del comments_list[i]['lower_comment_count']
                del comments_list[i]['upper_comment_id']
            return comments_list, True
        except Exception as e:
            print("[Error] (getUserCommentList)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return None, False

    def getUserLikeCommentList(self, user):
        """
        获得用户所有的评论
        :param user: 用户名
        :return: comment列表[{
            user:,
            star:,
            time:,
            likes:,
            text:,
            image:,
            class:,
            item_id:
        }]
        """
        try:
            # 获得相应评论id
            sql = "SELECT comment_id FROM user_like WHERE user = %s"
            val = (user,)
            self.cursor.execute(sql, val)
            comment_id_list = self.cursor.fetchall()
            # 获得相应评论
            sql = "SELECT * FROM comment WHERE id = %s"
            comments_list = []
            for id in comment_id_list:
                self.cursor.execute(sql, id)
                comments_list.append(self.cursor.fetchone())
            for i in range(len(comments_list)):
                comments_list[i] = self.tupleToDict(comments_list[i], COMMENT_KEY)
                del comments_list[i]['id']
                comments_list[i]['time'] = comments_list[i]['time'].strftime("%Y-%m-%d %H:%M:%S")
                del comments_list[i]['lower_comment_count']
                del comments_list[i]['upper_comment_id']
            return comments_list, True
        except Exception as e:
            print("[Error] (getUserLikeCommentList)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return None, False

    def checkItemCommented(self, user, item_class, item_id):
        """
        检查用户是否评论过某个item
        :param user: 用户名
        :param item_class: 所属模块
        :param item_id: id
        :return: 相应评论
        """
        try:
            # 获得相应评论
            sql = "SELECT * FROM comment WHERE class = %s AND item_id = %s AND user = %s"
            val = (item_class, item_id, user)
            self.cursor.execute(sql, val)
            raw_comment = self.cursor.fetchone()
            comment = self.tupleToDict(raw_comment, COMMENT_KEY)
            if comment != None:
                comment['time'] = comment['time'].strftime("%Y-%m-%d %H:%M:%S")
                return comment, True
            return None, False
        except Exception as e:
            print("[Error] (checkItemCommented)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return None, False

    # ==========后为功能性函数

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


db = MySQLDb(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)
