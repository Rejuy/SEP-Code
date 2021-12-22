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

    def reconnectDatabase(self):
        self.connection.reconnect(attempts=1, delay=0)

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

    def checkDataExistence(self, table, key, val):
        """
        检查数据是否存在
        :param table: 表名
        :param key: 键
        :param val: 值
        :return:
        """
        try:
            sql = "SELECT * FROM " + table + " WHERE " + key + "  = %s"
            get_val = (val,)
            # 使用 execute() 查询 email
            self.cursor.execute(sql, get_val)
            result = self.cursor.fetchone()
            if result:
                return True
            return False
        except Exception as e:
            print("[Error] (checkDataExistence)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def addUser(self, user_info):
        try:
            sql = "INSERT INTO user ("
            sql += self.getKeysStr(INSERT_USER_KEY) + ") VALUES " + self.producePlaceHolder(len(INSERT_USER_KEY))
            time = self.timeToStr(datetime.datetime.now())
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

    def getUserList(self, info):
        """
        返回给管理员用户列表
        :param info: {
            offset:,
            size:,
        }
        :return:
        """
        try:
            # 获得数据
            print(info)
            sql = "SELECT " + self.getKeysStr(ADMIN_GET_USER_KEY) + " FROM user"
            sql += " LIMIT " + str(info['size']) + " OFFSET " + str(info['offset'])
            self.cursor.execute(sql)
            print(198)
            user_list = self.cursor.fetchall()
            for i in range(len(user_list)):
                user_list[i] = self.tupleToDict(user_list[i], ADMIN_GET_USER_KEY)
                user_list[i]['account_birth'] = self.timeToStr(user_list[i]['account_birth'])
            return user_list, True
        except Exception as e:
            print("[Error] (getUserList)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return [], False

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

    def getData(self, table, locate_key, locate_value, get_key, get_all=True):
        """
        获取某条数据的某一些属性
        :param table: 表名
        :param locate_key: 定位的key（列表）
        :param locate_value: 定位的key对应的值（列表）
        :param get_key: 想要获取的key（列表）
        :return: 数据列表
        """
        try:
            # 获取数据
            sql = "SELECT " + self.getKeysStr(get_key) + " FROM " + table + " WHERE " + locate_key[0] + " = %s "
            val = (locate_value[0],)
            # print(len(locate_key))
            for i in range(1, len(locate_key)):
                sql += " and " + locate_key[i] + " = %s "
                val += (locate_value[i],)
            self.cursor.execute(sql, val)
            if get_all:
                data_list = self.cursor.fetchall()
                if len(data_list) == 0:
                    return [], False

                for i in range(len(data_list)):
                    data_list[i] = self.tupleToDict(data_list[i], get_key)
                    for key in get_key:
                        if type(data_list[i][key]) == datetime.datetime:
                            data_list[i][key] = self.timeToStr(data_list[i][key])
                return data_list, True
            else:
                data = self.cursor.fetchone()
                if not data:
                    return None, False
                data = self.tupleToDict(data, get_key)
                for key in get_key:
                    if type(data[key]) == datetime.datetime:
                        data[key] = self.timeToStr(data[key])
                return data, True
        except Exception as e:
            print("[Error] (getData)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            if get_all:
                return [], False
            else:
                return None, False

    def delItem(self, table, locate_key, locate_value, activated):
        """
        删除item
        :param table:
        :param locate_key: <list>
        :param locate_value: <list>
        :return:
        """
        try:
            # 定位
            locate = " WHERE " + locate_key[0] + " = %s "
            locate_val = (locate_value[0],)
            for i in range(1, len(locate_key)):
                locate += " AND " + locate_key[i] + " = %s "
                locate_val += (locate_value[i],)
            # 获得相应数据
            if activated:
                # key_list = ["user_id", "id"]
                sql = "SELECT user_id, id FROM " + table + locate
                self.cursor.execute(sql, locate_val)
                user_id, item_id = self.cursor.fetchone()
                # 更新其他表格数据
                # 用户表
                sql = "UPDATE user SET item_count = item_count - 1 WHERE id = %s"
                val = (user_id,)
                self.cursor.execute(sql, val)
                # 模块表
                sql = "UPDATE class SET count = count - 1 WHERE name = %s"
                class_name = table.split("_")[0][0].upper() + table.split("_")[0][1:]
                val = (class_name,)
                self.cursor.execute(sql, val)
                # TODO 评论表
            # 删除数据
            sql = "DELETE FROM " + table + locate
            self.cursor.execute(sql, locate_val)

            # 数据表内容更新
            self.connection.commit()
            return True
        except Exception as e:
            print("[Error] (delItem)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def addItem(self, table, item_info):
        """
        :param table: 表名
        :param item_info: item信息
        course{
            name: String ,
            teacher: String ,
            department: Int ,
            type: Int ,
            credit: Int ,
            schedule: Int ,
            user_id: Int
        }
        food{
            name: String ,
            position: String ,
            scope: Int ,
            hours: String ,
            type: Int ,
            user_id: Int
        }
        place{
            name: String ,
            position: String ,
            scope: Int ,
            hours: String ,
            type: Int ,
            user_id: Int
        }
        :return:
        """
        try:
            sql = "INSERT INTO " + table + " ("
            key_list, val = [], ()

            if table == "course_list":
                key_list = INSERT_COURSES_KEY
            elif table == "food_list":
                key_list = INSERT_FOOD_KEY
            elif table == "place_list":
                key_list = INSERT_PLACE_KEY

            if 'user_id' not in item_info.keys():
                item_info['activated'] = 1

            sql += self.getKeysStr(key_list) + ") VALUES " + self.producePlaceHolder(len(key_list))
            for key in key_list:
                try:
                    val += (item_info[key], )
                except:
                    if key == "time":
                        val += (self.timeToStr(datetime.datetime.now()), )
                    else:
                        val += (0, )
            # 写入新数据
            self.cursor.execute(sql, val)
            # 数据表内容更新
            self.connection.commit()
            return True
        except Exception as e:
            print("[Error] (addItem)：{}".format(e))
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
            like: (str)
            sort_order: (str)
            sort_criteria: (str)
            index_begin:
            item_count:
        }
        :return: list
        '''
        try:
            # 获得数据
            sql = "SELECT " + self.getKeysStr(info['key_list']) + " FROM " + table
            val = ()
            locate_sql = ""
            # 判断是否需要筛选，若是则加上筛选部分sql语句
            if len(info['filter']) != 0:
                locate_sql += " WHERE " + info['filter'][0]['key'] + " = %s "
                val += (info['filter'][0]['value'], )
                if len(info['filter']) > 1:
                    for i in range(1, len(info['filter'])):
                        locate_sql += " and " + info['filter'][i]['key'] + " = %s "
                        val += (info['filter'][i]['value'], )
                # 判断是否要模糊匹配
                if 'like' in info.keys() and info['like'] != "":
                    locate_sql += " AND (name LIKE '%" + info['like'] + "%' OR "
                    if table == "course_list":
                        locate_sql += "teacher LIKE '%" + info['like'] + "%') "
                    else:
                        locate_sql += "position LIKE '%" + info['like'] + "%') "
            else:
                # 判断是否要模糊匹配
                if 'like' in info.keys() and info['like'] != "":
                    locate_sql += " WHERE (name LIKE '%" + info['like'] + "%' OR "
                    if table == "course_list":
                        locate_sql += "teacher LIKE '%" + info['like'] + "%') "
                    else:
                        locate_sql += "position LIKE '%" + info['like'] + "%') "
            # 先根据条件获得数量
            count_sql = "SELECT COUNT(*) FROM " + table + locate_sql
            self.cursor.execute(count_sql, val)
            # 获得返回值
            count = self.cursor.fetchall()[0][0]
            # count = 0
            # 排序分页的数据量sql
            num_sql = ""
            # 判断是否需要排序，若是则加上排序部分sql语句
            if info['sort_order'] != "not_sort":
                num_sql += " order by " + info['sort_criteria'] + " "
                if info['sort_order'] == 'desc':
                    num_sql += 'desc '
                num_sql += " , id "
            # 进行分页操作
            num_sql += " LIMIT " + str(info['item_count']) + " OFFSET " + str(info['index_begin'])
            sql += locate_sql + num_sql
            print(sql)
            self.cursor.execute(sql, val)
            content_list = self.cursor.fetchall()
            return content_list, count, True
        except Exception as e:
            print("[Error] (getItemList)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return [], -1, False

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

    def getItem(self, table, table_id, info, key_list):
        """
        comments: {
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
            val = (info['id'], )
            self.cursor.execute(sql, val)
            raw_item = self.cursor.fetchone()
            # 转成字典
            item = self.tupleToDict(raw_item, key_list)
            # 获得相应评论
            sql = "SELECT COUNT(*) FROM comment WHERE class = %s AND item_id = %s"
            val = (table_id, info['id'])
            self.cursor.execute(sql, val)
            item['counts'] = self.cursor.fetchall()[0][0]
            item['negative'] = 0
            neutral_sql = sql + " AND star >= 2 AND star <= 3.5"
            self.cursor.execute(neutral_sql, val)
            item['neutral'] = self.cursor.fetchall()[0][0]
            positive_sql = sql + " AND star >= 4"
            self.cursor.execute(positive_sql, val)
            item['positive'] = self.cursor.fetchall()[0][0]
            if item['counts'] != 0:
                item['positive'] = int(item['positive'] / item['counts'] * 100)
                item['neutral'] = int(item['neutral'] / item['counts'] * 100)
                item['negative'] = 100 - item['positive'] - item['neutral']
            sql = "SELECT " + self.getKeysStr(ITEM_COMMENT_KEY) + " FROM comment WHERE class = %s AND item_id = %s ORDER BY likes desc, id  LIMIT " + str(info['count']) + " OFFSET " + str(info['begin'])
            self.cursor.execute(sql, val)
            comments_list = self.cursor.fetchall()

            for i in range(len(comments_list)):
                comments_list[i] = self.tupleToDict(comments_list[i], ITEM_COMMENT_KEY)
                comments_list[i]['date'] = self.timeToStr(comments_list[i]['time'])[0:10]
                del comments_list[i]['time']
                if len(comments_list[i]['text']) <= 50:
                    comments_list[i]['complete'] = 1
                    comments_list[i]['brief_text'] = comments_list[i]['text']
                    del comments_list[i]['text']
                else:
                    comments_list[i]['complete'] = 0
                    comments_list[i]['brief_text'] = comments_list[i]['text'][0: 50]
                    del comments_list[i]['text']
            item['comments'] = comments_list
            # 更新heat值
            sql = "UPDATE " + table + " SET heat = heat + 1 WHERE id = %s"
            val = (info['id'],)
            self.cursor.execute(sql, val)
            # 数据表内容更新
            self.connection.commit()
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
                        time = self.timeToStr(datetime.datetime.now())
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

    def delComment(self, key, val):
        # 不同方式删除用户（指定键值）
        try:
            # 首先获取信息
            info, flag = self.getData("comment", [key], [val], ["id", "class", "item_id", "user", "star"])
            info = info[0]

            # 更新其他表相应的值
            sql = "SELECT score, comment_count FROM " + INT_TO_TABLE[info['class']] + " WHERE id = %s"
            tval = (info['item_id'],)
            self.cursor.execute(sql, tval)
            result = self.cursor.fetchone()
            score = result[0]
            comment_count = result[1]
            if comment_count == 1:
                sql = "UPDATE " + INT_TO_TABLE[info['class']] + " SET score = 0, comment_count = 0, star = 0 WHERE id = %s"
                tval = (info['item_id'],)
                self.cursor.execute(sql, tval)  # 补上heat的更新
            else:
                score = (score * comment_count - 2 * info['star']) / (comment_count - 1)
                if score - int(score) >= 0.5:
                    new_score = int(score) + 1
                else:
                    new_score = int(score)
                star = new_score / 2
                sql = "UPDATE " + INT_TO_TABLE[info['class']] + " SET star = %s, score = %s, comment_count = comment_count - 1 WHERE id = %s"
                tval = (star, score, info['item_id'])
                self.cursor.execute(sql, tval)  # 补上heat的更新

            sql = "UPDATE user SET comment_count = comment_count - 1 WHERE user_name = %s"
            tval = (info['user'],)
            self.cursor.execute(sql, tval)

            # 数据表内容更新
            self.connection.commit()

            # 删除数据
            user_list, flag = self.getData("user_like", ["comment_id"], [info['id']], ["user"])
            for user in user_list:
                self.delLike(user['user'], info['id'], comment_deleted=True)

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
            time = self.timeToStr(datetime.datetime.now())
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

    def delLike(self, user, comment_id, comment_deleted=False):
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
            sql = "UPDATE user SET like_count = like_count - 1 WHERE user_name = %s"
            val = (user,)
            self.cursor.execute(sql, val)

            if not comment_deleted:
                sql = "UPDATE comment SET likes = likes - 1 WHERE id = %s"
                val = (comment_id,)
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
                comments_list[i]['time'] = self.timeToStr(comments_list[i]['time'])
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
                comments_list[i]['time'] = self.timeToStr(comments_list[i]['time'])
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

    def addCollection(self, class_id, item_id, user_id):
        """
        :param class_id: 模块的id,1,2,3
        :param item_id: item的id
        :param user_id: 用户的id
        :return:
        """
        try:
            name = self.getData(INT_TO_TABLE[class_id], ["id"], [item_id], ["name"])[0][0]['name']
            sql = "INSERT INTO user_favorite ("
            sql += self.getKeysStr(INSERT_COLLECTION_KEY) + ") VALUES " + self.producePlaceHolder(len(INSERT_COLLECTION_KEY))
            time = self.timeToStr(datetime.datetime.now())
            val = (user_id, class_id, item_id, time, name)
            # 写入新数据
            self.cursor.execute(sql, val)
            # 数据表内容更新
            self.connection.commit()
            # 更新其他表相应的值

            sql = "UPDATE user SET collection_count = collection_count + 1 WHERE id = %s"
            val = (user_id,)
            self.cursor.execute(sql, val)

            # 数据表内容更新
            self.connection.commit()
            return True
        except Exception as e:
            print("[Error] (addCollection)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def delCollection(self, class_id, item_id, user_id):
        """
        删除收藏
        :param class_id: 模块id
        :param item_id: item id
        :param user_id: user id
        :return: bool
        """
        try:
            # 删除数据
            sql = "DELETE FROM user_favorite WHERE class = %s AND item_id = %s AND user_id = %s"
            val = (class_id, item_id, user_id)
            self.cursor.execute(sql, val)
            # 数据表内容更新
            self.connection.commit()
            # 更新其他表相应的值

            sql = "UPDATE user SET collection_count = collection_count - 1 WHERE id = %s"
            val = (user_id,)
            self.cursor.execute(sql, val)

            # 数据表内容更新
            self.connection.commit()
            return True
        except Exception as e:
            print("[Error] (delCollection)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def checkItemCollected(self, class_id, item_id, user_id):
        """
        检查某一个item是否被收藏
        :param class_id: 模块id
        :param item_id: item id
        :param user_id: user id
        :return: bool
        """
        try:
            # 删除数据
            result, flag = self.getData("user_favorite", ["class", "item_id", "user_id"], [class_id, item_id, user_id], ["id"])
            return flag
        except Exception as e:
            print("[Error] (checkItemCollected)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

    def getGlobalItemList(self, info):
        '''
        :param info: {
            like: (str)
            sort_order: (str)
            sort_criteria: (str)
            index_begin:
            item_count:
        }
        :return: list
        '''
        try:
            # 获得数据
            data_sql = "SELECT * "
            count_sql = "SELECT COUNT(*) "
            locate_sql = "FROM (SELECT id, name, teacher as description, star, score, 1 FROM course_list WHERE name LIKE '%"\
                  + info['like']\
                  + "%' UNION SELECT id, name, position as description, star, score, 2  FROM food_list WHERE name LIKE '%"\
                  + info['like']\
                  + "%' UNION SELECT id, name, position as description, star, score, 3  FROM place_list WHERE name LIKE '%"\
                  + info['like']\
                  + "%') AS c "
            count_sql += locate_sql
            self.cursor.execute(count_sql)
            count = self.cursor.fetchall()[0][0]

            data_sql += locate_sql + "ORDER BY " + info['sort_criteria']
            if info['sort_order'] == 'desc':
                data_sql += ' DESC '
            data_sql += ", id "
            # 进行分页操作
            data_sql += " LIMIT " + str(info['item_count']) + " OFFSET " + str(info['index_begin'])
            self.cursor.execute(data_sql)
            item_list = self.cursor.fetchall()
            # 转化为字典
            for i in range(len(item_list)):
                item_list[i] = self.tupleToDict(item_list[i], GLOBAL_ITEM_KEY)
            return item_list, count, True
        except Exception as e:
            print("[Error] (getGlobalItemList)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return [], -1, False

    def selfChangeData(self, table, locate_key, locate_value, update_key, num):
        """
        使一个数据自增或自减
        :param table:
        :param locate_key: <list>
        :param locate_value: <list>
        :param update_key: str
        :param num: int
        :return:
        """
        try:
            # 定位
            locate = " WHERE " + locate_key[0] + " = %s "
            locate_val = (locate_value[0],)
            for i in range(1, len(locate_key)):
                locate += " AND " + locate_key[i] + " = %s "
                locate_val += (locate_value[i],)
            # 更新数据
            sql = "UPDATE " + table + " SET " + update_key + " = " + update_key + " + (" + str(num) + ")" + locate
            self.cursor.execute(sql, locate_val)
            self.connection.commit()
            return True
        except Exception as e:
            print("[Error] (selfChangeData)：{}".format(e))
            # 回滚所有更改
            self.connection.rollback()
            return False

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

    def timeToStr(self, raw_time):
        try:
            return raw_time.strftime("%Y-%m-%d %H:%M:%S")
        except:
            return ""
"""
    def select_db(self, sql):
        # 查询
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        # 使用 execute() 执行sql
        self.cur.execute(sql)
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        return data

    def execute_db(self, sql):
        # 更新/新增/删除
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
"""

db = MySQLDb(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)
