from flask import Flask, render_template
from mysql.connector import connection
import mysql.connector
from random import randrange

app = Flask(__name__)  
app.secret_key = "appLogin"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'roulettesadmin'
app.config['MYSQL_PASSWORD'] = 'admin'
from config_database import *
app.config['MYSQL_DB'] = 'roulette_database'

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