from mysql.connector import connection
import mysql.connector

connection = mysql.connector.connect(host="localhost", user="roulettesadmin", password="admin")
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS roulette_database")
cursor.close()
connection = mysql.connector.connect(host="localhost", user="roulettesadmin", password="admin", database="roulette_database")
cursor = connection.cursor()
cursor.execute("SHOW DATABASES")
database_exists = False
for database_name in cursor:
    if database_name[0]=="roulette_database": database_exists = True
if database_exists == True:
    print("The database EXISTS")
else:
    print("The database DOES NOT exist")

cursor.execute("CREATE TABLE IF NOT EXISTS roulettes (Id int NOT NULL AUTO_INCREMENT, State varchar(6) DEFAULT NULL, PRIMARY KEY(Id))")
cursor.execute("CREATE TABLE IF NOT EXISTS open_bets (Id int NOT NULL AUTO_INCREMENT, IdUsuario varchar(255) NOT NULL, IdRoulette int NOT NULL, BetSelection varchar(6) NOT NULL, BetAmount DECIMAL(7,2) NOT NULL, Datetime varchar(30) NOT NULL, PRIMARY KEY(Id))")
cursor.execute("CREATE TABLE IF NOT EXISTS closed_bets (Id int NOT NULL AUTO_INCREMENT, IdUsuario varchar(255) NOT NULL, IdRoulette int NOT NULL, BetSelection varchar(6) NOT NULL, BetAmount DECIMAL(7,2) NOT NULL, Datetime varchar(30) NOT NULL, BetResult varchar(5) NOT NULL, AmountWon DECIMAL(7,2) NOT NULL, PRIMARY KEY(Id))")
cursor.execute("CREATE TABLE IF NOT EXISTS bets_record (Id int NOT NULL AUTO_INCREMENT, IdUsuario varchar(255) NOT NULL, IdRoulette int NOT NULL, BetSelection varchar(6) NOT NULL, BetAmount DECIMAL(7,2) NOT NULL, Datetime varchar(30) NOT NULL, BetResult varchar(5) NOT NULL, AmountWon DECIMAL(7,2) NOT NULL, PRIMARY KEY(Id))")
cursor.close()