from services.mysql_service import db
import mysql.connector


if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host="49.233.1.189",
        user="root",
        passwd="123456",
        database="THUREC_db"
    )
    mycursor = mydb.cursor()

    sql = "UPDATE course_list SET schedule = 1"
    mycursor.execute(sql)
    sql = "UPDATE course_list SET activated = 1"
    mycursor.execute(sql)
    mydb.commit()

