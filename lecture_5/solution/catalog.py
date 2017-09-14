"""

catalog.csv data Expected columns in catalog file:

0. Иентификационен номер на артикула;
1. Наименование на артикула;
2. Цветове, в които артикулът е наличен;
3. Група на артикула;
4. Спорт, за който е предназначен артикулът;
5. Категория
6. Подкатегория
7. Пол, за който е предназначен артикула - мъже, жени, unisex, деца, бебета

Result:
    {
        item_id : category_name
        "J05705": "SHOES"
        ...

    }

"""
import csv

COLUMN_ITEM_ID = 0
COLUMN_CATEGORY = 5

def load_catalog(file_Path: str) ->  dict:

    result = {}

    with open(file_Path, 'r', encoding='utf-8') as csvfile:

        reader = csv.reader(csvfile)

        for row in reader:

            item_id = row[COLUMN_ITEM_ID]
            category = row[COLUMN_CATEGORY]
            result[item_id] = category

        return result
