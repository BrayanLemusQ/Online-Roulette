# Commit Purpose
This commits creates a function to search for an existing roulette, this changes allows to optimize the code used on `/RouletteOpening` and reuse it on `/AddBet`

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

### - routes.py
- `FindRoulette` function created to optimize code, this function receive as parameter only the id of the Roulette searched and return True or false depending on the roulette existence on the database. 
- `"/RouletteOpening"`route was changed to use the new function to verify the existence of the roulette.
- `"/AddBet"`route the variable name for id received was change to `roulette_id_received`
  

