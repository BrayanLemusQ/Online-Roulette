# Commit Purpose
 Table Creation and existence verification

# Operation

#### **Verify the existence of a database named *roulette_database* by typing the following lines on the virtual environment terminal, before running `flask run`:**

    mysql -u roulettesadmin -p

After that the terminal should show the following message

    Enter password: 

Insert the password: "**admin**"

You should be now on the mysql terminal, write the next code line

    SHOW DATABASES;

If the database *roulette_database* exists you can run flask as is mentioned below. If the database does not exist, type the following code line:

    CREATE DATABASE IF NOT EXISTS roulette_database


***Run the flask app by typing the following line:***

    flask run

Call the route *"/"* and verify that the table ***roulettes*** exists 

# Changes made compared to the previous one
- Table Creation 
- Additon of a random value to the table
- This version needs the creation of a database named *roulette_database*
- The operation process has changed

# Files and Folders
## Modified files and folders
### - app.py
- Table Creation 
- Addition of a random value syntax test
- Existence verification of a table
### - readme.md
-The operation process has changed, you should verify the existence of a database named *roulette_database* and if it does not exist you should create it (follow the steps in Operation)

