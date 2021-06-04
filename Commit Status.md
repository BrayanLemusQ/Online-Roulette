# Commit Purpose
Opening an existing roulette. The route `RouletteOpening` expects a `POST request` that gaves a valid `Roulette Id` to change the state of the respective roulette from *closed* to *open*

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


**Use the */AddBet* endpoint to create a new roulette**

**Use the */RouletteClosing* unused endpoint so far**

**Use the */RouletteList* unused endpoint so far**

# Changes made compared to the previous one
- Just the definition of `/RouletteOpening`, `/RoletteClosing` and `/RouletteList`, no code.



# Files and Folders
## Modified files and folders

### - routes.py
- the method `Get`  and `POST` have been defined in the route `"/RouletteOpening"`
- the code verifies the request made if is not POST, the endpoint will responses a messages like the one shown on the section *Operation* in this file. 
- key verification it must be `RouletteId` otherwise the endpoint will responses a messages like the one shown on the section *Operation* in this file. 
- Id verification it must be an Id of an existing roulette otherwise the endpoint will responses a messages like the one shown on the section *Operation* in this file. 
- If the verification process is succesfull, the state of the selected roulette changes to open, so bets can be done on it.

