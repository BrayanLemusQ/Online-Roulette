#from flask_mysqldb import MySQL
from mysql.connector import connection
import mysql.connector

connection = mysql.connector.connect(host="localhost", user="roulettesadmin", password="admin")
cursor = connection.cursor()
cursor.execute("DROP DATABASE IF EXISTS mydatabase")
cursor.execute("CREATE DATABASE IF NOT EXISTS roulette_database")
cursor.close()
connection = mysql.connector.connect(host="localhost", user="roulettesadmin", password="admin", database="roulette_database")
cursor = connection.cursor()
cursor.execute("SHOW DATABASES")
database_exists = False
for database_name in cursor:
    print(database_name[0])
    if database_name[0]=="roulette_database": database_exists = True
if database_exists == True:
    print("The database EXISTS")
else:
    print("The database DOES NOT exist")

cursor.execute("CREATE TABLE IF NOT EXISTS roulettes (id int unsigned NOT NULL, state varchar(6) DEFAULT NULL)")
cursor.execute("SHOW TABLES")
table_exists = False
for table_name in cursor:
    print(table_name[0])
    if table_name[0]=="roulettes": table_exists = True
if table_exists == True:
    print("The table EXISTS")
else:
    print("The table DOES NOT exist")