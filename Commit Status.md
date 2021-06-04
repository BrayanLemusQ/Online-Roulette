# Commit Purpose
This commits changes the open_bets table as the bet amount was missing. The new table columns are:
- Id 
- IdUsuario
- IdRoulette
- BetSelection
- BetAmount
- Datetime 

# Operation

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


**Use the */AddBet* so far the validation is limited just to verify the keys on the data received, if this results the data added to the database will be exactly the same received**

**Use the */RouletteClosing* unused endpoint so far**

**Use the */RouletteList* unused endpoint so far**

# Changes made compared to the previous one
- Definition of a new function in *routes.py* to optimize code



# Files and Folders
## Modified files and folders
### - config_database.py
- The open_bets table creation was changed due to a missing date. The bet amount was not specified. This changed was received succesfully on the database.

### - routes.py
- `VerifyBetAmount` function was created to evaluate the data from the requests. A valid value is considered between *0 - 10000* and it's only accepted integer values.
- the missing data was added to the insert on the `/AddBet` route 
  

