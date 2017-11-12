import sqlite3
from pprint import  pprint
# Connect to the db with the path to the db file

def main():
    with sqlite3.connect('./Northwind_small.sqlite') as connection:
        print_catalog(connection)
        new_employee_entry(connection, FirstName='Plamen', LastName='Hristov')
        print_catalog(connection)

# !!!!!!!!!! WRONG !!!!!!!! - POSIBILITY OF SQL INJECTION
def demo_sql_injection(connection):
    cursor = connection.cursor()
    print('DEMO Sql injection')
    first_name = "First Name"
    last_name = "Last Name"
    # !!!!!!!!! NEVER USE STRING FORMATING OR Concatanating(FirstName + LastName) with SQL Queries !!!!!!!!!!!!
    cursor.execute("insert into Employee(FirstName, LastName) values('{}', '{}')".format(first_name, last_name))


def new_employee_entry(connection, FirstName: str, LastName: str):
    cursor = connection.cursor()
    cursor.execute(
        'insert into Employee (FirstName, LastName) values (?, ?)', [FirstName, LastName]
    )

def print_catalog(connection):
    cursor = connection.cursor()
    cursor.execute('select * from Employee')
    #fetchall return a list with a tuple with the values of every columns from the table
    results = cursor.fetchall()

    for column_number, column in enumerate(results, start = 1):
        print('#{}'.format(column_number))
        print('\tid#{}'.format(column[0]))
        print('\tFirst Name {}'.format(column[1]))
        print('\tLast Name {}'.format(column[2]))
        print('\tJob Description {}'.format(column[3]))

        if column_number == 20:
            break;

if __name__ == '__main__':
    main()
