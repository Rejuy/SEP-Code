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
    #mycursor.execute("CREATE TABLE comment (id INT AUTO_INCREMENT PRIMARY KEY, class TINYINT, content_id INT, from_user_id INT, like_count INT, upper_comment_id INT, lower_comment_count INT, time DATETIME, star FLOAT, text TEXT, deleted TINYINT)")
    #sql = "alter table course_content modify column department INT"
    # 执行语句
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
    #mycursor.execute("alter table course_content add column click_count INT not null")
    #mycursor.execute("alter table comment default character set utf8")
    #mycursor.execute("alter table comment change text text text character set utf8")
    #mycursor.execute("alter table course_content change teacher teacher varchar(255) character set utf8")
    #mycursor.execute("CREATE TABLE class (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), count INT)")
    #mycursor.execute("CREATE TABLE food_content (id INT AUTO_INCREMENT PRIMARY KEY, type TINYINT, name VARCHAR(255), inside TINYINT, location VARCHAR(255), distance FLOAT, rate_count INT, rate FLOAT, heat FLOAT, comment_count INT, click_count INT)")
    #mycursor.execute("CREATE TABLE destination_content (id INT AUTO_INCREMENT PRIMARY KEY, type TINYINT, name VARCHAR(255), inside TINYINT, location VARCHAR(255), distance FLOAT, rate_count INT, rate FLOAT, heat FLOAT, comment_count INT, click_count INT)")
    sql = "INSERT INTO destination_content (type, name, inside, location, distance, rate_count, rate, heat, comment_count, click_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (1, "水木清华", 1, "熙春路东工字厅北", 0, 0, 0, 0, 0, 0)
    #val = [
    #    ('Course', 0),
    #    ('Food', 0),
    #    ('Destination', 0)
    #]
    # 写入新数据
    mycursor.execute(sql, val)
    # 数据表内容更新

    mydb.commit()
    # mycursor.execute("SHOW TABLES")


    # 数据表内容更新
    #mydb.commit()


