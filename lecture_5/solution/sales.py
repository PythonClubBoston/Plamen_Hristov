import csv
import iso8601

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

"""
Data for sales in files 'sales-*.csv'
Dанни за продажби - файлове 'sales-*.csv'
Файловете с продажби са във формат CSV (UTF-8), и съдържат следните колони:
Columns 
 0. Идентификационен номер на артикула;
 1. Държава, в която е била извършена продажбата (ISO code)
 2. Име на град, в която е била извършена продажбата;
 3. Дата/час на продажбата с timezone, във формат ISO8601;
 4. Цена на продажбата (цените на един и същ артикул в различните държави са различни)

 Result: list of dictionaries
     [
        {
            "item_id": "561712",
            "country": "ES",
            "city": "Murcia",
            "ts": datetime("2015, 12, 11, 17, 14, 05, tz=+01:00"),
            "price": 43.21
        },

        {
            ...
        }
     ]
"""

def load_sales(file_Path: str) -> list:

    result = []

    with open(file_Path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            sale = {}
            sale[KEY_ITEM_ID] = row[COLUMN_ITEM_ID]
            sale[KEY_COUNTRY] = row[COLUMN_COUNTRY]
            sale[KEY_CITY] = row[COLUMN_CITY]
            sale[KEY_TS] = iso8601.parse_date(row[COLUMN_TIMESTAMP])
            sale[KEY_PRICE] = float(row[COLUMN_PRICE])
            result.append(sale)
    return result

