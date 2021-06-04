# Online-Roulette
This repository implements an API that represents an online betting roulette. In this version there is a complete database configuration. This database contains two tables that stores the created roulettes and the bets that have been made. 
By using two specific endpoint you can add a new Roulette and a new Bet.

## Operation
Make sure the virtual environment is running. The word `(env)` should be at the beginning of the command line on the terminal as it shows the following line: 

    (env) PS C:\Desktop\Online-Roulette> 

If the virtual environment is not running type the following line on the terminal

    .\env\Scripts\Activate.ps1

#### **No database existence verification need**

***Run the flask app by typing the following line:***

    flask run

**Use the */AddRoulette* endpoint to create a new roulette as a result it will send a json data with the following structure**

    {
    "created_roulette_id": created_roulette_id,
    "response": 200
    }
The `created_roulette_id` type is `int`

**Use the */RouletteOpening* endpoint to change a roulette state from closed to open, that will allow the roulette to accept bets.**
Make sure to use a `POST REQUEST` with the following json structure:

    {
        "RouletteId": valid_roulette_id_number
    }
The `valid_roulette_id_number` should be `int`

The only valid key in the `JSON` structure is `RouletteId`, if the request does not brings this data, the endpoint will respond:

    {
        "Update": "Failed",
        "error": "Invalid Key",
        "response": 400
    }

In addition, if the id number send as a `RouletteId` has not been created jet, the endpoint will respond:

    {
        "Update": "Failed",
        "error": "Invalid Id",
        "response": 400
    }

A succesful roulette opening should look like this:

    {
        "RouletteState": "open",
        "Update": "Succesful",
        "response": 200
    }


**Use the */AddBet* endpoint to create a new roulette**

**Use the */RouletteClosing* unused endpoint so far**

**Use the */RouletteList* unused endpoint so far**
