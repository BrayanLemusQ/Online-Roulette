# Commit Purpose
This commits defines the `RoulettesList` route to list the existing roulettes in the table `roulettes`. If the table `roulettes`is empty the route will respond with a empty data, otherwise the route will list all the created roulettes.


# Operation

#### **¬ No database existence verification need**


### ***¬ Run the flask app by typing the following line:***
    
    flask run

### **¬ Use the */AddRoulette* endpoint** to create a new roulette as a result it will send a json data with the following structure*

    {
    "created_roulette_id": created_roulette_id,
    "response": 200
    }
The `created_roulette_id` type is `int`

### **¬ Use the */RouletteOpening* endpoint** to change a roulette state from closed to open, that will allow the roulette to accept bets.
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

The response to a succesful roulette opening should look like this:

    {
        "RouletteState": "open",
        "Update": "Succesful",
        "response": 200
    }


### **¬ Use the */AddBet* endpoint to** save a new bet value on the database `open_bets` 
In this endpoint there are certain conditions that must be verified to make a succesful bet add.
#### Conditions
- the bet would be added only to an **existing roulette**
- the bet amount is an integer between ***"0 - 10000"***
- the bet selection by the user is a number between ***"0 - 36"*** or a color ***"black"*** or ***"red"***
- the bet would be addet to an ***open roulette***

Make sure to make a `POST request` with the following data:

    {
        "RouletteId": valid_roulette_id_number,
        "BetSelection": valid_bet_selection,
        "BetAmount": valid_bet_amount
    }
The `POST request` must have the following `HEADER`:

    "headers": { "IdUsuario" : valid_user_id }

- The `valid_roulette_id_number` must be an integer
- The `valid_bet_selection` must be a number between ***"0 - 36"*** or a color ***"black"*** or ***"red"***, this value must be a string
- The `valid_bet_amount` must be an integer between ***"0 - 10000"***

If any of the above values do not meet the listed conditions *(wrong type, value out of range, etc)* or the `RouletteId` corresponds to a closed roulette, the endpoint will respond:

    {
        "Added Bet": "Failed",
        "error": "Invalid Received Values",
        "response": 400
    }

Pay attention to the *key values* in the *JSON format*, if the request does not brings this data, the endpoint will respond:

    {
        "Added Bet": "Failed",
        "error": "Invalid Key or Header",
        "response": 400
    }

The response to a bet successfully added should look like this:

    {
        "Added Bet": "Succesful",
        "response": 200
    }

### **¬ Use the */RouletteClosing* to** unused endpoint so far

### **¬ Use the */RoulettesList* to** list all the created roulettes with theyre corresponding status. 

The route will send a respond with a Json data using the following structure as a result for the request. You must use a `GET request` to acquire the data.

    {
        "roulette_id_1": current_roulette_status,
        "roulette_id_2": current_roulette_status,
        "roulette_id_3": current_roulette_status,

        .
        .
        .

        "roulette_id_n": current_roulette_status,
    }

If the table `roulettes`is empty you will receive a empty data:

    {}



# Changes made compared to the previous one
- A `RoulettesList` route was created
- The route in charge of listing the created roulettes has changed its name from `RouletteList` to `RoulettesList`


# Files and Folders
## Modified files and folders

### - routes.py
- the `AdquireDateNowISOFormat` function is created. The package `DateTime` is imported to the file so the methods `astimezone()` and `isoformat()` gets the current date and stores it in the format as required.
  - *Example: 2020-04-21T13:09:24-05:00*
- This function is called after values verification, its result is stored on the variable `date_adquired` to insert it in the table using the query previously created.
