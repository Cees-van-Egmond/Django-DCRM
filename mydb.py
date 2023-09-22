# install MySQL on your computer
# http://dev.mysql.com/downloads/installer/
# pip install mysql
# pip mysql-coonnector
# pip mysql-coonnector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Mxstream12'
    )

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE dcrm_table")

print("All Done!")
