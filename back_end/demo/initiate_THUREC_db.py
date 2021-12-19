import mysql.connector


if __name__ == "__main__":
    # 创建数据库
    '''
    mydb = mysql.connector.connect(
        host="49.233.1.189",
        user="root",
        passwd="123456"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE THUREC_db")
    mycursor.close()
    mydb.close()
    '''

    # 连接数据库
    mydb = mysql.connector.connect(
        host="49.233.1.189",
        user="root",
        passwd="123456",
        database="THUREC_db"
    )
    mycursor = mydb.cursor()
    print("测试")
    #sql = 'SELECT id, name, teacher, department, type, star, score FROM course_list order by star LIMIT 0,16 '
    #order by star
    #mycursor.execute(sql)
    #print(mycursor.fetchall())
    #mycursor.execute("CREATE TABLE comment (id INT AUTO_INCREMENT PRIMARY KEY, class TINYINT, content_id INT, from_user_id INT, like_count INT, upper_comment_id INT, lower_comment_count INT, time DATETIME, star FLOAT, text TEXT, deleted TINYINT)")
    #sql = "INSERT INTO place_list (name, range) VALUES (%s, %s)"
    #val = ('第二教室楼', 1)
    # 执行语句
    #mycursor.execute(sql, val)
    #mydb.commit()
    #sql = "UPDATE course_list SET comment_count = 1, credit = 2, heat = 0 WHERE id = 1"
    #sql = "SELECT place_list.name, food_list.name, course_list.name FROM place_list, food_list, course_list WHERE place_list.name LIKE '%清%' OR food_list.name LIKE '%清%' OR course_list.name LIKE '%清%'"
    sql = "select * from (select id, name, teacher as description, star, score, 1 from course_list where name like '%清%' " \
          "union select id, name, star, position as description, score, 3 from place_list where name like '%清%' " \
          "union select id, name, star, position as description, score, 2 from food_list where name like '%清%') as c order by star desc, id limit 10 offset 0"
    mycursor.execute(sql)
    print(mycursor.fetchall())
    """
    mycursor.execute("alter table destination_content default character set utf8")
    mycursor.execute("alter table destination_content change name name varchar(255) character set utf8")
    mycursor.execute("alter table destination_content change location location varchar(255) character set utf8")
    mycursor.execute("alter table food_content default character set utf8")
    mycursor.execute("alter table food_content change name name varchar(255) character set utf8")
    mycursor.execute("alter table food_content change location location varchar(255) character set utf8")
    """
    #mycursor.execute(sql)
    #mydb.commit()
    #print(mycursor.fetchall()[0][0])
    #mycursor.execute("alter table comment add column content_id INT not null")
    #mycursor.execute("alter table comment default character set utf8")
    #mycursor.execute("alter table comment change text text text character set utf8")
    #mycursor.execute("alter table comment change id id int character set utf8")
    #mycursor.execute("CREATE TABLE class (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), count INT)")
    #mycursor.execute("CREATE TABLE food_content (id INT AUTO_INCREMENT PRIMARY KEY, type TINYINT, name VARCHAR(255), inside TINYINT, location VARCHAR(255), distance FLOAT, rate_count INT, rate FLOAT, heat FLOAT, comment_count INT, click_count INT)")
    #mycursor.execute("CREATE TABLE destination_content (id INT AUTO_INCREMENT PRIMARY KEY, type TINYINT, name VARCHAR(255), inside TINYINT, location VARCHAR(255), distance FLOAT, rate_count INT, rate FLOAT, heat FLOAT, comment_count INT, click_count INT)")
    #sql = "INSERT INTO destination_content (type, name, inside, location, distance, rate_count, rate, heat, comment_count, click_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #val = (1, "水木清华", 1, "熙春路东工字厅北", 0, 0, 0, 0, 0, 0)
    #val = [
    #    ('Course', 0),
    #    ('Food', 0),
    #    ('Destination', 0)
    #]
    # 写入新数据
    #mycursor.execute(sql, val)
    # 数据表内容更新

    #mydb.commit()
    # mycursor.execute("SHOW TABLES")


    # 数据表内容更新
    #mydb.commit()


