from flask.wrappers import Request
from app import app
from mysql.connector import connection
import mysql.connector
from flask import request, jsonify

connection = mysql.connector.connect(host="localhost", user="roulettesadmin", password="admin", database="roulette_database")

def FindRoulette(id):
    cursor = connection.cursor()
    query = "SELECT Id FROM roulettes WHERE Id = %s"
    cursor.execute(query,[id]) 
    roulette_id_found = cursor.fetchone()
    if roulette_id_found != None: return True
    else: return False

def VerifyBetAmount(bet_amount):
    valid_bet_amount=False
    if type(bet_amount) == int or type(bet_amount) == float:
        if bet_amount in range(0,10000):
            valid_bet_amount=True
    return valid_bet_amount

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
            roulette_id_received = request_json_data['RouletteId']
            roulette_found=FindRoulette(roulette_id_received)
            if roulette_found:
                query = "UPDATE roulettes SET State = 'open' WHERE Id = %s"
                cursor.execute(query,[roulette_id_received])
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
        
        if 'RouletteId' in request_json_data and 'BetSelection' in request_json_data and 'IdUsuario' in request_headers and 'BetAmount' in request_json_data:
            roulette_id_received = request_json_data['RouletteId']
            roulette_found=FindRoulette(roulette_id_received)
            bet_selection = request_json_data['BetSelection']
            bet_amount = request_json_data['BetAmount']
            id_usuario = request_headers['IdUsuario']
            query = "INSERT INTO open_bets (IdUsuario, IdRoulette, BetSelection, BetAmount, Datetime) VALUES (%s,%s,%s,%s,%s)"
            bet_values = [id_usuario, roulette_id_received, bet_selection, bet_amount, "1997-07-16T19:20:30.45+01:00"]
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



