from flask import Flask, render_template
from flask_mysqldb import MySQL 

app = Flask(__name__)   
app.secret_key = "appLogin"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'roulettesadmin'
app.config['MYSQL_PASSWORD'] = 'admin'
mysql = MySQL(app)


@app.route("/")
def index():
    cursor=mysql.connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS roulette_database")
    cursor.execute("DROP DATABASE IF EXISTS tempdb")
    cursor.execute("SHOW DATABASES")
    database_exists = False
    for database_name in cursor:
        print(database_name[0])
        if database_name[0]=="roulette_database": database_exists = True
    if database_exists == True:
        return "The database EXISTS"
    else:
        return "The database DOES NOT exist"
    
