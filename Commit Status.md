# Commit Purpose
This commits saves the valid bets on a database. If the `IdRoulette` exists and this roulette is open, the beth would be consider as a valid bet. So far, the code allows to create a bet if the request send a header and a structure with the valid keys. The validation of the data received is missing.

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
- Just the definition of `/RouletteOpening`, `/RoletteClosing` and `/RouletteList`, no code.



# Files and Folders
## Modified files and folders

### - routes.py
- the method `Get` is deleted in `"/RouletteOpening"`, is not need it.
- the method `POST` have been defined in the route `"/AddBet"`.
- the following changes were made on the  `"/AddBet"` route.
  - the code verifies the request made, if is not POST the endpoint will responses a messages like the one shown on the section *Operation* in this file. 
  - key verification, it should exists `RouletteId` `Bet` and `IdUsuario` otherwise the endpoint will responses a message of invalid keyvalue.
  

