from app import app
from mysql.connector import connection
import mysql.connector
from flask import request, jsonify
import datetime

connection = mysql.connector.connect(host="localhost", user="roulettesadmin", password="admin", database="roulette_database")

def FindRoulette(id):
    valid_roulette = False
    cursor = connection.cursor()
    query = "SELECT Id FROM roulettes WHERE Id = %s"
    cursor.execute(query,[id]) 
    roulette_id_found = cursor.fetchone()
    if roulette_id_found != None: valid_roulette = True
    else: valid_roulette = False
    return valid_roulette

def VerifyBetAmount(bet_amount):
    valid_bet_amount=False
    if type(bet_amount) == int:
        if bet_amount in range(0,10000): 
            valid_bet_amount=True
    return valid_bet_amount

def VerifyBetSelection(bet_selection):
    valid_bet_amount=False
    if type(bet_selection) == str:
        valid_bet_selection=list(range(39))
        for valid_numbers in range(37):
            valid_bet_selection[valid_numbers]=str(valid_bet_selection[valid_numbers])
        valid_bet_selection[37]='black'
        valid_bet_selection[38]='red'
        tuple(valid_bet_selection)
        times_selection_appears__in_valid_selection=valid_bet_selection.count(bet_selection)
        if times_selection_appears__in_valid_selection == 1:
            valid_bet_amount=True
    return valid_bet_amount

def VerifyRouletteStatus(id):
    roulette_status_open = False
    cursor = connection.cursor()
    query = "SELECT State FROM roulettes WHERE Id = %s"
    cursor.execute(query,[id]) 
    roulette_found_state = cursor.fetchone()
    if roulette_found_state != None:
        if roulette_found_state[0] == 'open': 
            roulette_status_open = True
    return roulette_status_open

def AdquireDateNowISOFormat():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    datetime_iso8601_format= datetime.datetime(year, month, day, hour, minute, second).astimezone().isoformat()
    return datetime_iso8601_format

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
            bet_selection = request_json_data['BetSelection']
            bet_amount = request_json_data['BetAmount']
            id_usuario = request_headers['IdUsuario']
            roulette_found=FindRoulette(roulette_id_received)   
            bet_amount_correct = VerifyBetAmount(bet_amount)
            bet_selection_correct = VerifyBetSelection(bet_selection)
            roulette_status_open = VerifyRouletteStatus(roulette_id_received)
            if roulette_found and bet_amount_correct and bet_selection_correct and roulette_status_open:
                date_adquired=AdquireDateNowISOFormat()
                query = "INSERT INTO open_bets (IdUsuario, IdRoulette, BetSelection, BetAmount, Datetime) VALUES (%s,%s,%s,%s,%s)"
                bet_values = [id_usuario, roulette_id_received, bet_selection, bet_amount, date_adquired]
                cursor.execute(query, bet_values)
                connection.commit()
                return jsonify({'response':200,'Added Bet':"Succesful"})
            else:
                return jsonify({'response':400,'Added Bet':"Failed",'error':"Invalid Received Values"})
        else:
            return jsonify({'response':400,'Added Bet':"Failed",'error':"Invalid Key or Header"})

@app.route("/RouletteClosing")
def RouletteClosing():
    return "Roulette Closed"

@app.route("/RoulettesList", methods = ["GET"])
def RoulettesList():
    cursor = connection.cursor()
    query = "SELECT * FROM roulettes"
    cursor.execute(query)
    roulettes_created = cursor.fetchall()
    dictionary_roulette ={} 
    if cursor.rowcount != 0:
        for row_id_roulettes in roulettes_created:
            dictionary_roulette[row_id_roulettes[0]]= row_id_roulettes[1]
    return jsonify(dictionary_roulette)
