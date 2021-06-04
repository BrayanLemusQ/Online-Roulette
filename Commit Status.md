# Commit Purpose
 Optimization code. A new configuration database file was added to the project thanks to the MySQL Connector/Python version, so there is no more need to verify the existence of a database since the code can do it by itself with this new file.

# Operation

#### **No database existence verification need**

***Run the flask app by typing the following line:***

    flask run


# Changes made compared to the previous one
- New configuration file created that is responsible for verification an creation of the database. It also allows to create tables and the basic database structure, this reduces *app.py* code and separate functionalities.
- Table Creation in case it did not exist
- Database Creation in case it did not exist
- The operation process has been optimized

# Files and Folders
## Modified files and folders
### - app.py
- Import the configuration from the *config_database.py* file
- Code reduced. 
- 
### - readme.md
-The operation process has changed, you should not verify the existence of a database named *roulette_database*

## Created files and folders
### - confid_database.py
- This file is created to centralize the entire database configuration .
- It creates a database *roulette_database* in case it did not exists
- It creates a table *roulettes* in case it did not exists

### - flask-MySqldb 
- removed extension
### - mysql.connector
- installed extension
