from app import app
from mysql.connector import connection, cursor
import mysql.connector
from flask import request, jsonify
import datetime
import random

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
    bet_amount_type = type(bet_amount)
    if bet_amount_type == int or bet_amount_type == float:
        integer_part_bet_amount, decimal_part_bet_amount = divmod(bet_amount, 1)
        if integer_part_bet_amount in range(0,10000): 
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

def TableColumnNames(table_name):
    if table_name == "roulettes": query = "SHOW COLUMNS FROM roulettes"
    if table_name == "open_bets": query = "SHOW COLUMNS FROM open_bets"
    if table_name == "closed_bets": query = "SHOW COLUMNS FROM closed_bets"
    cursor = connection.cursor()    
    cursor.execute(query)
    table_column_names=cursor.fetchall()

    return table_column_names

def ListTableRecords(table_name):
    column_names_data = TableColumnNames(table_name)
    existing_table_records = TableRecords(table_name)
    noumber_of_records = len(existing_table_records) 
    records_list = [None]*noumber_of_records
    record_from_the_table={}  
    record_number=0
    for row_elements in existing_table_records:
        column_number=0
        for column_name_data in column_names_data:
            column_name = column_name_data[0]
            if column_name == "BetAmount" or column_name == "AmountWon":
                record_from_the_table[column_name_data[0]]= float(row_elements[column_number])
            else:
                record_from_the_table[column_name_data[0]]= row_elements[column_number]
            column_number+=1
        records_list[record_number] = record_from_the_table
        record_from_the_table={}
        record_number+=1
        
    return records_list

def TableRecords(table_name):
    if table_name == "roulettes": query = "SELECT * FROM roulettes"
    if table_name == "open_bets": query = "SELECT * FROM open_bets"
    if table_name == "closed_bets": query = "SELECT * FROM closed_bets"
    cursor = connection.cursor()
    cursor.execute(query)
    table_records = cursor.fetchall()

    return table_records

def WinningResultSelection():
    valid_bet_selection=list(range(39))
    for valid_numbers in range(37):
        valid_bet_selection[valid_numbers]=str(valid_bet_selection[valid_numbers])
    valid_bet_selection[37]='black'
    valid_bet_selection[38]='red'
    valid_bet_selection = tuple(valid_bet_selection)
    winning_tuple_position = random.randint(0,38)
    winning_value = valid_bet_selection[winning_tuple_position]

    return winning_value

def CreateResultTable(id):
    bet_result = WinningResultSelection()
    query = "SELECT * FROM open_bets WHERE IdRoulette = %s"
    cursor = connection.cursor()
    cursor.execute(query,[id])
    elements_created = cursor.fetchall() 
    if elements_created != []:
        for row_id_elements in elements_created:
            table_user_id = row_id_elements[1]
            table_bet_selection = row_id_elements[3]
            table_bet_amount = float(row_id_elements[4])
            table_datetime = row_id_elements[5]
            if table_bet_selection == bet_result:
                if table_bet_selection == "black" or table_bet_selection == "red":
                    amount_won = 1.8 * table_bet_amount
                else:
                    amount_won = 5 * table_bet_amount
            else:   amount_won =  0
            cursor = connection.cursor()
            query = "INSERT INTO closed_bets (IdUsuario, IdRoulette, BetSelection, BetAmount, Datetime, BetResult, AmountWon) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            bet_values = [table_user_id, id, table_bet_selection, table_bet_amount, table_datetime, bet_result, amount_won]
            cursor.execute(query, bet_values)
            connection.commit()

def SaveClosedBetsRecord(Id):
    cursor = connection.cursor()
    transfer_closed_bets_into_record_query = "INSERT INTO bets_record SELECT * FROM closed_bets"   
    cursor.execute(transfer_closed_bets_into_record_query)
    delete_closed_bets_query = "DELETE FROM closed_bets"    
    cursor.execute(delete_closed_bets_query)
    delete_open_bets_query = "DELETE FROM open_bets WHERE IdRoulette = %s"
    cursor.execute(delete_open_bets_query,[Id])
    connection.commit()

def CloseRoulette(Id):
    cursor = connection.cursor()
    close_roulette_query = "UPDATE roulettes SET State = 'closed' WHERE Id = %s"
    cursor.execute(close_roulette_query,[Id])
    connection.commit()  

@app.route("/")
def index():
    return "Use the Following routes /AddRoulette, /RouletteOpening, /AddBet, /RouletteOpening or /RoulettesList"

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

@app.route("/RouletteClosing", methods=["POST"])
def RouletteClosing():
    cursor = connection.cursor()
    if request.method == "POST":
        request_json_data = request.json
        if 'RouletteId' in request_json_data:
            roulette_id_received = request_json_data['RouletteId']
            roulette_found=FindRoulette(roulette_id_received)
            roulette_status_open = VerifyRouletteStatus(roulette_id_received)
            if roulette_found and roulette_status_open:
                CreateResultTable(roulette_id_received)
                closed_bets_record = ListTableRecords("closed_bets")
                CloseRoulette(roulette_id_received)
                SaveClosedBetsRecord(roulette_id_received)
                return jsonify(closed_bets_record)
            else:
                return jsonify({'response':400,'Update':"Roulette Closing",'error':"Invalid Id"})            
        else:
            return jsonify({'response':400,'Update':"Roulette Closing",'error':"Invalid Key"})
    else:
        return jsonify({'response':405,'Update':"Roulette Closing",'error':"Invalid Method"})

@app.route("/RoulettesList", methods = ["GET"])
def RoulettesList():
    created_table_list=ListTableRecords("roulettes")
    return jsonify(created_table_list)




    







