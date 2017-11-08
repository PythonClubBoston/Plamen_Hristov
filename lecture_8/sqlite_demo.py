import sqlite3
from pprint import  pprint
# Connect to the db with the path to the db file

with sqlite3.connect('./Northwind_small.sqlite') as connection:
    cursor = connection.cursor()
    cursor.execute('select * from Employee')
    #fetchall return a list with a tuple with the values of every columns from the table
    results = cursor.fetchall()
    pprint(results)