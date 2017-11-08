import sqlite3

# Connect to the db with the path to the db file

connection = sqlite3.connect('./Northwind_small.sqlite')

resultset = connection.execute('select * from Employee order by BirthDate')