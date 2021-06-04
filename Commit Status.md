# Commit Purpose
Using a route to add a new bet

# Operation

#### **No database existence verification need**

***Run the flask app by typing the following line:***

    flask run

**Use the */AddRoulette* endpoint to create a new roulette**

**Use the */AddBet* endpoint to create a new Bet**

# Changes made compared to the previous one
- Addition of a new table `roulettes` to the database
- Addition of a new table `open_bets` to the database
- Addition of a new bet in the `open_bets` table using a route


# Files and Folders
## Modified files and folders
### - app.py
-A new *"/AddBet* route was created
- INSERT query was used to insert a new Bet with random information to the  `open_bets` table
- 
### - config_database.py
- The `open_bets` table was created.

