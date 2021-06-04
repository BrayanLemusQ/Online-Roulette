from app import app
from mysql.connector import connection
import mysql.connector

@app.route("/")
def index():
    return "Check the terminal"

@app.route("/AddRoulette")
def AddRoulette():
    connection = mysql.connector.connect(host="localhost", user="roulettesadmin", password="admin", database="roulette_database")
    cursor = connection.cursor()
    query = "INSERT INTO roulettes (state) VALUES (%s)"
    cursor.execute(query, ["closed"])
    connection.commit()
    cursor.close()
    return "Roulette Created "

@app.route("/RouletteOpening")
def RouletteOpening():
    return "Roulette Opened"

@app.route("/AddBet")
def AddBet():
    connection = mysql.connector.connect(host="localhost", user="roulettesadmin", password="admin", database="roulette_database")
    cursor = connection.cursor()
    query = "INSERT INTO open_bets (IdUsuario, IdRoulette, Bet, Datetime) VALUES (%s,%s,%s,%s)"
    values = ["a",str(1),"30","1997-07-16T19:20:30.45+01:00"]
    cursor.execute(query, values)
    connection.commit()
    cursor.close()

    return "Bet Added"

@app.route("/RouletteClosing")
def RouletteClosing():
    return "Roulette Closed"

@app.route("/RouletteList")
def RouletteList():
    return "Roulette list displayed"



