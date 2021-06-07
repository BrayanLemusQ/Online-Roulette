# Online-Roulette
This repository implements an `API` that represents an ***online betting roulette***. In this version there is a complete configuration to open new roulettes, bet on it, closed these roulettes and get results. The operation, parameters, received information and more are shown below (It is recommended to read the entire operation in order to use the `API` correctly).

## Operating Principle

The Online-Roulette meets the following functions.
- Creates new roulettes with an unique Id
- Open existing roulettes. You must open a roulette before betting on it.
- List existing roulettes and show theire status
- Each roulette has the following betting option:
  - Numbers between **0 - 36** (*Just integers*)
  - Colors: **"black"** or **"red"**
    - You can only choose ***one number or one color by bet***. (If you want to choose both you should make one bet for a number and one bet for a color)
- Close an existing open roulette. This step choose an aleatory number or color and send the respective bets with the results.
  - Hit the right number pays 5 times the bet
  - Hit the color pays 1.8 times the bet 

Bet operation result:
  - You can pick **either a number or a color**. 
  - The program select a **number as a winner**.
  - The program will determine if the winning **number is odd or even**. 
  - If you pick the **"black" color**, you would win if the result is an **odd number**
  - If you pick the **"red" color**, you would win if the result is an **even number**

## Operation

The database where the data would be stored is created automatically. Add the following user with all the priviliges in mysql server

    HOST : 'localhost'
    USER : 'roulettesadmin'
    PASSOWORD : 'admin' 

Make sure the virtual environment is running on your terminal. The word `(env)` should be at the beginning of the command line on the terminal as it shows the following line: 

    (env) PS C:\Desktop\Online-Roulette> 

If the virtual environment is not running type the following line on the terminal

    .\env\Scripts\Activate.ps1


### **¬ Run the flask app by typing the following line:***

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

If any of the above values do not meet the listed conditions *(wrong type, value out of range, etc)* or the `RouletteId`corresponds to a closed roulette, the endpoint will respond:

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

    [
    {
        "Id": roulette_id_1,
        "State": current_roulette_status
    },
    {
        "Id": roulette_id_2,
        "State": current_roulette_status
    },
    .
    .
    .
    {
        "Id": roulette_id_n,
        "State": current_roulette_status
    },

If the table `roulettes`is empty you will receive a empty data:

    {}

