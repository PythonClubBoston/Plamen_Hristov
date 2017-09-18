import csv
import itertools
from pprint import pprint

def load_catalog(filename: str):
    result = []
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
           result.append(row)
    return result

catalog = load_catalog('catalog.csv')
# pprint(catalog)

catalog.sort(key=lambda row: row[-2])

for grouped_value, grouper in itertools.groupby(catalog, key=lambda row: row[-2]):
    print(grouped_value)
    for row in grouper:
        print(row)
    print('-'*100)
    print('-'*100)
    print('-'*100)

#help(itertools.groupby)