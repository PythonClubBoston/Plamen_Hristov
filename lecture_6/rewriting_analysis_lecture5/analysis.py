import csv
from datetime import datetime
from pprint import pprint
import itertools
import functools
import iso8601

CATALOG_FILE_PATH = 'catalog.csv'
SALES_FILE_PATH = 'sales-10K.csv'

def load_catalog(catalog_path: str) -> dict: #return dictionaries {'item_id': 'J11328', 'category':'SHOES'}
    KEY_ID = 0
    KEY_CATEGORY = 5
    catalog_categories = {}

    with open(catalog_path, 'r', encoding='utf-8') as f:

        reader = csv.reader(f)
        for row in reader:
            catalog_categories[row[KEY_ID]] = row[KEY_CATEGORY]
        return catalog_categories
""" load_sales(sales_path)
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

KEY_COLUMN_ID = 'item_id'
KEY_COLUMN_COUNTRY = 'country'
KEY_COLUMN_CITY = 'city'
KEY_COLUMN_TS = 'ts'
KEY_COLUMN_PRICE = 'price'

KEY_ROW_ID = 0
KEY_ROW_COUNTRY = 1
KEY_ROW_CITY = 2
KEY_ROW_TS = 3
KEY_ROW_PRICE = 4

def load_sales(sales_path: str) -> list:

    with open (sales_path, 'r', encoding='utf-8') as f:

        reader  = csv.reader(f)
        for row in reader:
            sale = {}
            sale[KEY_COLUMN_ID] = row[KEY_ROW_ID]
            sale[KEY_COLUMN_COUNTRY] = row[KEY_ROW_COUNTRY]
            sale[KEY_COLUMN_CITY] = row[KEY_ROW_CITY]
            sale[KEY_COLUMN_TS] = iso8601.parse_date(row[KEY_ROW_TS])
            sale[KEY_COLUMN_PRICE] = float(row[KEY_ROW_PRICE])
            yield sale

def top_sales_by_cities(sales):

    sales_by_city = {}

    for sale in sales:
        city = sale['city']
        price = float(sale['price'])

        if city not in sales_by_city :
            sales_by_city[city] = 0
        sales_by_city[city] += price

    top_sales_by_cities_sorted = []

    for sale, city in sales_by_city.items():
        top_sales_by_cities_sorted.append((sale, city))

    top_sales_by_cities_sorted.sort(reverse=True)

    for city, sale in top_sales_by_cities_sorted:
        print('{} : {: .2f}'.format(city, sale))

def print_top_by_hour(sales):

    best_sales_by_hour = {}

    for sale in sales:
        ts = sale['ts'].replace(minute=0, second=0, microsecond=0)
        price = float(sale['price'])

        if ts not in best_sales_by_hour:
            best_sales_by_hour[ts] = 0

        best_sales_by_hour[ts] += price

    best_sales_by_hour_sorted = []

    for ts, price in best_sales_by_hour.items():
        best_sales_by_hour_sorted.append((price, ts))

    best_sales_by_hour_sorted.sort(reverse=True)

    for price, hour in best_sales_by_hour_sorted[:5]:
        print('{}: {: .2f}  €'.format(hour, price))

def main():
    catalogs = load_catalog(CATALOG_FILE_PATH)
    sales = load_sales(SALES_FILE_PATH)
    top_sales_by_cities(sales)
    summary_sales(sales)
    print_top_by_hour(sales)

    total_count = 0
    total_amount = 0
    min_timestamp = None
    max_timestamp = None
    amount_by_categories = {}

    load_sales_generator_object = load_sales(SALES_FILE_PATH)

    for sale in load_sales_generator_object:

        #summary
        total_amount += sale['price']
        total_count += 1
        ts = sale['ts']
        if min_timestamp is None or ts < min_timestamp:
            min_timestamp = ts

        if max_timestamp is None or ts > max_timestamp:
            max_timestamp = ts
        average_sale = total_amount / total_count

        #top by category

        id = sale['item_id']
        price = float(sale['price'])
        category_name = catalogs.get(id, None)
        if category_name not in amount_by_categories:
            amount_by_categories[category_name] = 0
        amount_by_categories[category_name] += price

        sorted_amount_by_categories = []

        sorted_amount_by_categories = list(amount_by_categories.items())
        sorted_amount_by_categories.sort(key=lambda el: el[1], reverse=True)

        #print top sales by cities

        sales_by_city = {}

        city = sale['city']
        price_by_city = float(sale['price'])

        if city not in sales_by_city :
            sales_by_city[city] = 0
        sales_by_city[city] += price_by_city

    top_sales_by_cities_sorted = []

    for sale, city in sales_by_city.items():
        top_sales_by_cities_sorted.append((sale, city))

    top_sales_by_cities_sorted.sort(reverse=True)

    # for city, sale in top_sales_by_cities_sorted[:5]:
    #     print('{} : {: .2f}'.format(city, sale))

    #print for summary
    print("""
Обобщение
---------
Общ брой продажби: {}
Общо сума продажби: {: .2f} €
Средна цена на продажба: {: .2f} €
Начало на период на данните: {}
Край на период на данните: {}
        """.format(total_count, total_amount, average_sale,
        min_timestamp, max_timestamp))

    #print for top sales by category
    for accumulated_sells, category_name in sorted_amount_by_categories[:5]:
        print('{} : {: .2f} €'.format(accumulated_sells, category_name))


main()

