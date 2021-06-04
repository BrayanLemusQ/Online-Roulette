# Commit Purpose
Instalation of `request` libraries used to send the `id` of a new roulette everytime is created 

# Operation

#### **No database existence verification need**

***Run the flask app by typing the following line:***

    flask run

**Use the */AddRoulette* endpoint to create a new roulette as a result it will send a json data with the following structure**

    {
    "created_roulette_id": created_roulette_id,
    "response": 200
    }

**Use the */AddBet* endpoint to create a new Bet**

# Changes made compared to the previous one
- Just the definition of `/RouletteOpening`, `/RoletteClosing` and `/RouletteList`, no code.



# Files and Folders
## Modified files and folders

### - routes.py
- Modules `request` and `jsonify` from flask have been imported
- the method `Get` has been defined in the route `"/AddRoulette"`
- the last id created has been captured and sended as a response to the request with the following JSON format

    {
    "created_roulette_id": created_roulette_id,
    "response": 200
    }


