# Commit Purpose
This commits modifies the `/AddBet` route to save a new bet once the received data has been verified. This routes uses differente function to verify the following conditons:
- the bet would be added only to an **existing roulette**
- the bet amount is an integer between ***"0 - 10000"***
- the bet selection by the user is a number between ***"0 - 36"*** or a color ***"black"*** or ***"red"***
- the bet would be addet to an ***open roulette***

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

### **¬ Use the */RouletteList* to** unused endpoint so far

# Changes made compared to the previous one
- Definition of a new function in *routes.py* to optimize code



# Files and Folders
## Modified files and folders
### - config_database.py
- The open_bets table creation was changed due to a missing date. The bet amount was not specified. This changed was received succesfully on the database.

### - routes.py
- `VerifyBetSelection` function was created to evaluate the bet selection from the requests. A valid value is considered between *"0 - 36"* and *"black"* or *"red"*. Given that the bet can be either a number or a color, a `str` list is created to store the numbers and two addional values that correspond to the black and red position. The list is converted to a tuple so a received value as a `bet_selection` can be found on the tuple, if the value exits the `times_selection_appears__in_valid_selection` would be one, in that case the `bet_selection` is correct and the function will return a `True` value, otherwise the returned value will be `False` 
  - The `bet_selection` value received must be a string, otherwise the returned value will be `False`.
- `FindRoulette` function was created to search a existing roulette, the query returns a  `None` value when the searched id does not exist, based on this if the returned valued is different it means that the roulette exists, in that case the function will return a `True` value, otherwise the returned value will be `False` 
  - The `id` value received must be an intenger, otherwise the returned value will be `False`.
- The `VerifyBetAmount`function was created to check that the received value is an integer between *"0 - 10000"*, in that case the function will return a `True` value, otherwise the returned value will be `False` 
  - The `bet_amount` value received must be an intenger, otherwise the returned value will be `False`.
- The `VerifyRouletteStatus` function was created to verify that the roulette status is open, the query was created to search into the `roulettes` table the `id` received and acquire the roulette status

