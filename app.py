from flask import Flask, render_template
from flask_mysqldb import MySQL 

app = Flask(__name__)  
app.secret_key = "appLogin"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'roulettesadmin'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'roulette_database'
mysql = MySQL(app)


@app.route("/")
def index():
    cursor=mysql.connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS roulette_database")
    cursor.execute("CREATE TABLE IF NOT EXISTS roulettes (id int unsigned NOT NULL, state varchar(6) DEFAULT NULL)")
    query = "INSERT INTO roulettes(id, state) VALUES (%s, %s)"
    cursor.execute(query,(str(1),"closed"))
    mysql.connection.commit()
    cursor.execute("SHOW TABLES")
    table_exists = False
    for table_name in cursor:
        print(table_name[0])
        if table_name[0]=="roulettes": table_exists = True
    cursor.execute("DESCRIBE roulettes")
    cursor.close()
    if table_exists == True:
        return "The table EXISTS"
    else:
        return "The table DOES NOT exist"
