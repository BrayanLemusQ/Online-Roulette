# Online-Roulette
This repository implements an API that represents an online betting roulette

## Operation
Make sure the virtual environment is running. The word `(env)` should be at the beginning of the command line on the terminal. 

    (env) PS C:\Desktop\Online-Roulette> 

If the virtual environment is not running type the following line on the terminal

    .\env\Scripts\Activate.ps1

#### **Verify the existence of a database named *roulette_database* by typing the following lines on the virtual environment terminal, before running `flask run`:**

    mysql -u roulettesadmin -p

After that the terminal should show the following message

    Enter password: 

Insert the password: "**admin**"

You should be now on the mysql terminal, write the next code line

    SHOW DATABASES;

If the database *roulette_database* exists you can run flask as is mentioned below. If the database does not exist, type the following code line:

    CREATE DATABASE IF NOT EXISTS roulette_database


***Run the flask app by typing the following line:***

    flask run
