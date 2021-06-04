# Commit Purpose
Using a route to add a new roulette

# Operation

#### **No database existence verification need**

***Run the flask app by typing the following line:***

    flask run


# Changes made compared to the previous one
- Addition of a new element to the database

# Files and Folders
## Modified files and folders
### - app.py
-A new *"/AddRoulette* route was created
- INSERT query was used to insert a new roulette with the state as closed by default. 
- 
### - confid_database.py
- The *id* of the table roulettes was changed to auto-increment and it was set as a *PRIMARY KEY*
- The existence table verification code was deleted

