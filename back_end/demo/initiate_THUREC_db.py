import mysql.connector


if __name__ == "__main__":
    # 创建数据库

    mydb = mysql.connector.connect(
        host="49.233.1.189",
        user="root",
        passwd="123456"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE THUREC_db")
    mycursor.close()
    mydb.close()


    # 连接数据库
    mydb = mysql.connector.connect(
        host="49.233.1.189",
        user="root",
        passwd="123456",
        database="THUREC_db"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, user_name VARCHAR(255), password VARCHAR(255), email VARCHAR(255), account_birth DATETIME, collection_count INT, like_count INT, comment_count INT, content_count INT, activated TINYINT, introduction TEXT)")
    # mycursor.execute("SHOW TABLES")


