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

### **¬ Use the */RouletteClosing* to** search the bets made in a specific roulette, and send the results as a response:

Make sure to make a `POST request` with the following data:

    {
        "RouletteId": valid_roulette_id_number
    }
- The `valid_roulette_id_number` must be an integer

If the `IdRoulette` sended in the `request` corresponds to a table without any bets the response will be an empty data:

    {}

If the `IdRoulette` sended in the `request` corresponds to an none-existing roulette the response will be the following:

    {
        "Roulette Closing": "Failed",
        "error": "Invalid Id",
        "response": 400
    }

Pay attention to the *key values* in the *JSON format*, if the request does not brings this data, the endpoint will respond:

    {
        "Roulette Closing": "Failed",
        "error": "Invalid Key or Header",
        "response": 400
    }

The response to a succesfully roulette closing will be like this:

    [
    {
        "AmountWon": amoun_won,
        "BetAmount": bet_amount,
        "BetResult": bet_result,
        "BetSelection": bet_selection,
        "Datetime": datetime,
        "Id": bet_closed_id,
        "IdRoulette": id_roulette,
        "IdUsuario": id_usuario
    }
    ]


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

If the table `roulettes` is empty you will receive an empty data:

    {}

This route must be completed this are the functionalities missing:

- Closed the roulette selected 
- Delete the previous data before adding the new closed_bets
- Delete the betf of the table closed in the open bets table


# Changes made compared to the previous one
- A `RoulettesList` route was created
- The route in charge of listing the created roulettes has changed its name from `RouletteList` to `RoulettesList`


# Files and Folders
## Modified files and folders

### - routes.py

- `TableRecords` function is created to optimize the code, everytime the complete record information of a table is required, this function can be called, sending the name of the table to be consulted as a parameter. Inside the function, the query required is created based on the sended parameter, in this way the function would always return the right information.
  - This `function` return a `list` type value.
  - Every list position corresponds to a recorded data in the table consultes.
  - Every list position contents a `tuple`. This `tuple` represents the information stores at the time of registration
  - The table name is received in the function as a `string`
  
- `TableColumnNames` function is created. This function returns the name of the table received as a parameter.
  - This `function` return a `list` type value.
  - Every list position contents a `tuple`. This `tuple` represents the information of the column (*`int, null, PRIMARY KEY, varchar(n), etc...`*). 
  - The first position of every `tuple` represents each column name.
  - The table name is received in the function as a `string`

- `ListTableRecords` function is created. This function returns the records list from a specifc table. The table name must be passed as a paremeter to the function.
  - This `function` return a `list` type value.
  - Every list position contents a `dictionary`. This `dictionary` represents the store record information
  - Creates a dictionary for every record information and uses the returned value in `TableColumnNames` as `key parameter` to the dictionary and the read values from the table as the value stored 
  - A single record is stored as a `dictionary`, and the complete record is stored as a `list` of this dictionaries.
  - The table name is received in the function as a `string`

- `WinningResultSelection` function is created. This function creates a `tuple` that stores the possible values to bet; the numbers between **0 - 36** and the colors **black** and **red**. It also generates a random `int` value between  **0 - 38**, this number determines the `winning_value` stored in the `winner_tuple_position`.
- The winning value is returned as a string.

- `CreateResultTable` function is created. This function creates an entire table record (the table structured is defined in the `config_database.py` file), the record value corresponds to the information of every bet made in a specific roulette, adiotining two fields `BetResult` (indicates the winning value for this specific roulette) and `AmountWon`(indicates the amount won in that bet, if the `BetResult` is not the same that the `BetSelection` this value will be *0*)
  -   This function does not return any value since the information is stored in the database on a specific table called `closed_bets`
  -   This `function` select the information in the `open_bets` table that corresponds to an specific `roulette id` (the parameter recieved in this function), this information is copied to `closed_bet` table aditioning the values mentioned above.
  -   This `function` also validates if the `BetSelection` is equal to the `BetResult`, in that case the `AmountWon` will be `BetAmount` multiplied 5 times if `BetSelection` was a number and 2 times if it was a color. 
  -   ***Important*** this function must be modified since the `AmountWon` should be multiplied 1.8 times instead 2. It is not like this jet becouse it requires a change in the definition of `AmountWon` on the `closed_bets` creation (`AmountWon` as a `float`  rather than `integer`).

- `/RoulettesList` was changed. This function uses the `ListTableRecords` function created to optimize its code.


- `/RouletteClosing` route was added. This `route` is in charge  of searching the bets made in a specific roulette, and send the results as a response with the following structrure:
  -   There is a first validation of the method `request`. This must be a `GET request`
  -   The route validates the existence of the roulette based on the `IdRoulette` received on the request
  -   The route verifies the `status` of the table, if its closed the process wont go on.
  -   The route call the function `CreateResultTable` passing the `IdRoulette` received on the request to acquire the bets made in this roulette and check for a winner
  -   The route call the function `ListTableRecords` to acquire the record of the closed bets, and send it as a response.

