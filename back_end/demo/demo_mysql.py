import mysql.connector


if __name__ == "__main__":

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Rjy20008172#",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    # mycursor.execute("CREATE DATABASE mydatabase")
    # mycursor.execute("SHOW DATABASES")
    # for x in mycursor:
    #     print(x)

    # mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)
    # mycursor.execute("ALTER TABLE customers ADD COLUMN introduction TEXT")

    sql = "INSERT INTO customers (name, address, introduction) VALUES (%s, %s, %s)"
    val = ('Enjoy77', 'THU', "Hi everybody! My name is Enjoy, and it's so damn fucking happy to meet you stupid guys. You know what? I am actually here to kill you.")

    mycursor.execute(sql, val)

    mydb.commit()

    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

