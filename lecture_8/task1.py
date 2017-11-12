# Import the data for the sales from CSV file into the data base
# When you using the code from the previous lecture.
# Use the modules from the previous lecture containing CatalogEntry and Sale




# cursor.execute("""
#     create table if not exists catalog(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     item_key varchar(200),
#     category varchar(200),
# """)
# );

import sys
import sqlite3
import csv
import iso8601

DB_FILENAME = 'sales-database.db'
CATALOG_FILENAME = 'catalog.csv'
SALES_FILENAME = 'sales-10K.csv'

COLUMN_ITEM_ID = 0
COLUMN_CATEGORY = 5

COLUMN_ITEM_ID = 0
COLUMN_COUNTRY = 1
COLUMN_CITY = 2
COLUMN_TIMESTAMP = 3
COLUMN_PRICE = 4

KEY_ITEM_ID = 'item_id'
KEY_COUNTRY = 'country'
KEY_CITY = 'city'
KEY_TS = 'ts'
KEY_PRICE = 'price'

def main():
    # check isolation_level
    with sqlite3.connect(DB_FILENAME, isolation_level=None) as connection:
        print('Connection opened')
        create_tables(connection)
        print('Tables created')
        # load_catalog_into_db(CATALOG_FILENAME, connection)
        # print('Catalog csv file inserted into category db table')
        load_sales_into_db(SALES_FILENAME, connection)
        print('Sales loaded into the db')
def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS sale
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_key varchar(200) NOT NULL,
        country varchar(3),
        city_name varchar(80),
        sale_timestamp TEXT,
        price NUMERIC
    )
    
    """ )
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS category
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_key varchar(200),
        category varchar(200)
    )
    
    """)

def load_catalog_into_db(filename: str, connection) -> dict:
    cursor = connection.cursor()
    result = {}

    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            item_id = row[COLUMN_ITEM_ID]
            category = row[COLUMN_CATEGORY]
            result[item_id] = category

        for item_key, category in result.items():
            cursor.execute(
                """
                    INSERT INTO category (item_key, category) values ( ?, ?) 
                """, [item_key, category]
            )

def load_sales_into_db(file_Path: str, connection):
    cursor = connection.cursor()
    with open(file_Path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            item_key = row[COLUMN_ITEM_ID]
            country = row[COLUMN_COUNTRY]
            city_name = row[COLUMN_CITY]
            sale_timestamp = iso8601.parse_date(row[COLUMN_TIMESTAMP])
            price = float(row[COLUMN_PRICE])
            cursor.execute(
                """
                INSERT INTO sale ( item_key, country, city_name, sale_timestamp, price) 
                values (?,?,?,?,?)""", [item_key, country, city_name, sale_timestamp, price] )

if __name__ == '__main__':
    main()