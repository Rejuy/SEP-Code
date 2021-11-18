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
    #mycursor.execute("alter table course_content add column comment_count INT not null")
    #mycursor.execute("alter table user default character set utf8")
    #mycursor.execute("alter table user change user_name user_name varchar(255) character set utf8")
    #mycursor.execute("alter table course_content change teacher teacher varchar(255) character set utf8")
    #mycursor.execute("CREATE TABLE class (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), count INT)")
    #mycursor.execute("CREATE TABLE course_content (id INT AUTO_INCREMENT PRIMARY KEY, number INT, type TINYINT, name VARCHAR(255), teacher VARCHAR(255), department VARCHAR(255), schedule VARCHAR(255), rate_count INT, rate FLOAT, heat FLOAT)")
    #sql = "INSERT INTO class (name, count) VALUES (%s, %s)"
    #val = [
    #    ('Course', 0),
    #    ('Food', 0),
    #    ('Destination', 0)
    #]
    # 写入新数据
    #mycursor.executemany(sql, val)
    # 数据表内容更新
    #mydb.commit()
    # mycursor.execute("SHOW TABLES")


