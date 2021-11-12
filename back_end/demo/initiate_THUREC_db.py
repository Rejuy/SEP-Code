import mysql.connector


if __name__ == "__main__":
    # 创建数据库
    '''
     mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Rjy20008172#"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE THUREC_db")
    mycursor.close()
    mydb.close()
    '''

    # 连接数据库
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Rjy20008172#",
        database="THUREC_db"
    )
    mycursor = mydb.cursor()
    # mycursor.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, user_name VARCHAR(255), password VARCHAR(255), email VARCHAR(255), account_birth DATETIME, collection_count INT, like_count INT, comment_count INT, content_count INT, portrait LONGBLOB, activated TINYINT)")
    # mycursor.execute("SHOW TABLES")
    mycursor.execute("ALTER TABLE user ADD COLUMN introduction TEXT")

