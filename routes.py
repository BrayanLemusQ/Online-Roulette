from flask.wrappers import Request
from app import app
from mysql.connector import connection
import mysql.connector
from flask import request, jsonify

connection = mysql.connector.connect(host="localhost", user="roulettesadmin", password="admin", database="roulette_database")

@app.route("/")
def index():
    return "Check the terminal"

@app.route("/AddRoulette", methods=["GET"])
def AddRoulette():
    cursor = connection.cursor()
    query = "INSERT INTO roulettes (state) VALUES (%s)"
    cursor.execute(query, ["closed"])
    connection.commit()
    created_roulette_id = cursor.lastrowid 
    cursor.close()
    return jsonify({'response':200,'created_roulette_id':created_roulette_id})
    
@app.route("/RouletteOpening", methods=["POST"])
def RouletteOpening():
    cursor = connection.cursor()
    if request.method == "POST":
        request_json_data = request.json
        if 'RouletteId' in request_json_data:
            query = "SELECT Id FROM roulettes WHERE Id = %s"
            cursor.execute(query,[request_json_data['RouletteId']]) 
            roulette_id_found = cursor.fetchone()
            if roulette_id_found != None:
                query = "UPDATE roulettes SET State = 'open' WHERE Id = %s"
                cursor.execute(query,[request_json_data['RouletteId']])
                connection.commit()  
                return jsonify({'response':200,'Update':"Succesful",'RouletteState':'open'})
            else:
                return jsonify({'response':400,'Update':"Failed",'error':"Invalid Id"})            
        else:
            return jsonify({'response':400,'Update':"Failed",'error':"Invalid Key"})
    else:
        return jsonify({'response':405,'Update':"Failed",'error':"Invalid Method"})

@app.route("/AddBet", methods=["POST"])
def AddBet():
    cursor = connection.cursor()
    if request.method == "POST":
        request_json_data = request.json
        request_headers=request.headers
        if 'RouletteId' in request_json_data and 'Bet' in request_json_data and 'IdUsuario' in request_headers:
            roulette_id = request_json_data['RouletteId']
            bet = request_json_data['Bet']
            id_usuario = request_headers['IdUsuario']
            query = "INSERT INTO open_bets (IdUsuario, IdRoulette, Bet, Datetime) VALUES (%s,%s,%s,%s)"
            bet_values = [id_usuario,roulette_id,bet,"1997-07-16T19:20:30.45+01:00"]
            cursor.execute(query, bet_values)
            connection.commit()
            return "Bet Added - Correct Data"
        else:
            return jsonify({'response':400,'Update':"Failed",'error':"Invalid Key or Header"})
    else:
        return jsonify({'response':405,'Update':"Failed",'error':"Invalid Method"})

@app.route("/RouletteClosing")
def RouletteClosing():
    return "Roulette Closed"

@app.route("/RouletteList")
def RouletteList():
    return "Roulette list displayed"



