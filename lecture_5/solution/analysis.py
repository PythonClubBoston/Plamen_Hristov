"""
Разполагаме с каталог на стоки и данни за продажби на голям производител на спортни стоки,
и трябва да направим анализ на тази информация.
Крайната цел на задачата е да анализираме данните и да визуализираме:
    $ python3    analyze.py   catalog.csv   sales-10K.csv

    Обобщение
    ---------
        Общ брой продажби: 10000
        Общо сума продажби: 3191507.82 €
        Средна цена на продажба: 319.15 €
        Начало на период на данните: 2015-12-01T08:00:48+01:00
        Край на период на данните: 2016-01-24T20:49:38+00:00

    Сума на продажби по категории (top 5)
    -----------------------------
        SHOES: 1519077.15 €
        T-SHIRTS: 207615.78 €
        HEADWEAR: 176304.77 €
        BALLS: 146092.19 €
        JACKETS: 130226.14 €

    Сума на продажби по градове (top 5)
    -----------------------------
        Manchester: 100620.74 €
        Liverpool: 96607.68 €
        London: 92239.71 €
        Nottingham: 90084.01 €
        Glasgow: 87052.21 €

    Сума на продажби по час (top 5)
    -----------------------------
        2015-12-01 12:00:00+01:00: 9209.70 €
        2016-01-17 10:00:00+02:00: 8811.59 €
        2016-01-05 20:00:00+01:00: 8590.52 €
        2015-12-29 20:00:00+02:00: 8270.59 €
        2016-01-05 10:00:00+01:00: 8028.91 €

    Обърнете внимание, че часът от последния анализ трябва да бъде в UTC часова зона - "+00:00".
----------------
Входни данни и описание на формат на данните
    Продуктов каталог - файл 'catalog.csv'
    Файловете с продуктовия каталог са във формат CSV (UTF-8), и съдържа следните колони:

        Идентификационен номер на артикула;
        Наименование на артикула;
        Цветове, в които артикулът е наличен;
        Група на артикула;
        Спорт, за който е предназначен артикулът;
        Категория
        Подкатегория
        Пол, за който е предназначен артикула - мъже, жени, unisex, деца, бебета

    Примерни редове от файла с каталога:

        "538352","TYGUN II","BLACK/RUNNINWHT","FOOTWEAR","BOXING","SHOES","SHOES (LOW)","Men"
        "42259","M TEAM TEE","WHITE/DARKNAVY","TEXTILES","TENNIS","T-SHIRTS","T-SHIRT (SHORT SLEEVE)","Men"
        "562319","NOVA WALK 06","DARONX/METSIL/DSHALE","FOOTWEAR","WALKING","SHOES","SHOES (LOW)","Men"
        "G13130","COMPOUND","BLACK1/BLACK1/LGTIPD","FOOTWEAR","GOLF","SHOES","SHOES (LOW)","Men"
        "396559","+TG SWERVE DBMI","WHITE/BLACK","HARDWARE","FOOTBALL/SOCCER","BALLS","BALL (MACHINE-STITCHED)","Men"
        "34549","LTA SS2G C","RUNWHI/SHABLU/VAPOUR","FOOTWEAR","BASKETBALL","SHOES","SHOES (LOW)","Kid"
--------------
Данни за продажби - файлове 'sales-*.csv'
Файловете с продажби са във формат CSV (UTF-8), и съдържат следните колони:
    Идентификационен номер на артикула;
        Държава, в която е била извършена продажбата (ISO code)
        Име на град, в която е била извършена продажбата;
        Дата/час на продажбата с timezone, във формат ISO8601;
        Цена на продажбата (цените на един и същ артикул в различните държави са различни)

Примерни редове от файл с продажби:
    "561712","ES","Murcia","2015-12-11T17:14:05+01:00",43.21
    "K81938","FR","Nantes","2016-01-14T20:58:38+01:00",36.57
    "41975","IT","Catania","2016-01-12T10:57:50+01:00",409.58
    "538352","DE","Düsseldorf","2015-12-18T20:50:21+01:00",95.03
==============
Насоки
    Parse на дати в ISO8601 формат
        За да parse-нете датите във файловете с продажби, използвайте модула iso8601

        import iso8601
        ...
        dt = iso8601.parse_date('2015-12-11T17:14:05+01:00')
        print(dt)
        2015-12-11 17:14:05+01:00

    Работа с datetimes, които съдържат информация за часови зони
        Вземане на текуща дата/час в часова зона UTC

        from datetime import datetime, timezone

        now_utc = datetime.now(tz=timezone.utc)
        print(now_utc)
        '2016-01-26 14:38:02.720755+00:00'

    Конвертиране към от друга часова зона към UTC
        from datetime import datetime, timezone
        import iso8601

        d = iso8601.parse_date('2015-12-18T20:50:21+01:00')
        print(d)
        '2015-12-18 20:50:21+01:00'

        d_in_utc = d.astimezone(timezone.utc)
        print(d_in_utc)
        '2015-12-18 19:50:21+00:00'
"""





"""
TASK
1. Load catalog file
2. Load the sales file
"""




from pprint import pprint

from lecture_5.solution.catalog import load_catalog
from lecture_5.solution.sales import load_sales, KEY_TS, KEY_PRICE, KEY_ITEM_ID

CATALOG_FILE_PATH = '/home/plamen/PycharmProjects/lecture_5/solution/catalog.csv'
SALES_FILE_PATH = '/home/plamen/PycharmProjects/lecture_5/solution/sales-10K.csv'



def print_total_stats(sales):

        total_amount = 0
        total_count = len(sales)

        min_timestamp = None
        max_timestamp = None


        for sale in sales:  #see sales.load_sales() for details
            total_amount += sale[KEY_PRICE]
            ts = sale[KEY_TS]

            if min_timestamp is None or ts < min_timestamp:   #alt min(sale['ts'] for sale in sales) 
                min_timestamp = ts

            if max_timestamp is None or ts > max_timestamp:
                 max_timestamp = ts

        print("""
      Обобщение                                                 
      ---------                                                 
          Общ брой продажби: {total_count}                              
          Общо сума продажби: {total_amount: .2f}                     
          Средна цена на продажба: {average_price: .2f} €                     
          Начало на период на данните: {min_ts}
          Край на период на данните: {max_ts} 
             """.format(
        total_count = total_count,
        total_amount = total_amount,
        average_price = total_amount / total_count if total_count else None,
        min_ts = min_timestamp,
        max_ts = max_timestamp
    )
          )
def print_top_by_category(sales, catalog):

    amounts_by_category = {} # key: category_name, value: accumulated sum of sales

    for sale in sales:
        item_id = sale[KEY_ITEM_ID]
        price = sale[KEY_PRICE]
        category_name = catalog.get(item_id, None)

        if category_name not in amounts_by_category:
            amounts_by_category[category_name] = 0

        amounts_by_category[category_name] += price

    amounts_by_category_sorted = []


    for category_name, total_amount in amounts_by_category.items():
        amounts_by_category_sorted.append((total_amount, category_name))

    amounts_by_category_sorted.sort(reverse=True)

    print("""Сума на продажби по категории (top 5) 
-----------------------------""")

    for total_amount, category_name in amounts_by_category_sorted[:5]:
        print("     {}: {: .2f} €".format(category_name, total_amount))

def print_top_by_city(sales):

    """
        Сума на продажби по градове (top 5)
        -----------------------------
            Manchester: 100620.74 €
            Liverpool: 96607.68 €
            London: 92239.71 €
            Nottingham: 90084.01 €
            Glasgow: 87052.21 €
    """

    sales_by_city = {}

    for sale in sales:
        city = sale['city']       #in constant
        price = sale['price']

        if city not in sales_by_city:
            sales_by_city[city] = 0

        sales_by_city[city] += price

    sales_by_city_sorted = []

    for top_city, top_sales in sales_by_city.items():
        sales_by_city_sorted.append((top_sales, top_city))

    sales_by_city_sorted.sort(reverse=True)

    for top_sales, top_city in sales_by_city_sorted[:5]:
        print(' {}: {:.2f} €'.format(top_city, top_sales))

def print_top_by_hour(sales):
    pass
"""
    Сума на продажби по час (top 5)
    -----------------------------
        2015-12-01 12:00:00+01:00: 9209.70 €
        2016-01-17 10:00:00+02:00: 8811.59 €
        2016-01-05 20:00:00+01:00: 8590.52 €
        2015-12-29 20:00:00+02:00: 8270.59 €
        2016-01-05 10:00:00+01:00: 8028.91 €
"""

def main():

    catalog = load_catalog(CATALOG_FILE_PATH)
    #pprint(catalog)
    sales = load_sales(SALES_FILE_PATH)

    #print_total_stats(sales)
    #print_top_by_category(sales, catalog)
    print_top_by_city(sales)
    print_top_by_hour(sales)

main()