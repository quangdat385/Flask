import mysql.connector

mydb= mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="783151")

my_cursor=mydb.cursor()

# my_cursor.execute("CREATE DATABASE our_users")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)



# pip install mysql-connector
# pip install mysql-connector-python
# pip install mysql-connector-python-rf
# pip install pymysql
# pip install cryptography