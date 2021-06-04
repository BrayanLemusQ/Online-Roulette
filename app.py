from flask import Flask, render_template

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