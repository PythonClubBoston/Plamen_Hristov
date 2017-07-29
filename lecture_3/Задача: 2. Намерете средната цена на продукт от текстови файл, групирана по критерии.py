"""


Използвайки кода си от предишната задача, и използвайки същите файлове, намерете средната цена от всички продукти в каталога, групирани по пол/възраст.
Използвайте колоната №6 за пол и възраст.

catalog_sample.csv

catalog_full.csv

Структурата на CSV файловете е следната:

каталожен номер
име на продукта
цветове на продукта. Ако са повече от един са разделени с /
за какъв вид активност е предназначен артикула
каква е групата на артикула
за кой пол и възраст е предназначен артикула
цена
Разделителят на данните е , (запетая), а десеттичният знак е . (точка).

"""

def extract_info_in_a_list(path_to_info_as_string): # return list with the info for the products
    with open(path_to_info_as_string, 'r') as catalog_with_products:
        catalog_list_with_products = []

        for line in catalog_with_products:
            #https://stackoverflow.com/questions/3849509/how-to-remove-n-from-a-list-element
            catalog_list_with_products.append(line.strip())

        return catalog_list_with_products

def extract_prices_by_gender(list_of_products): #return list with prices categoriesed by gender for concrete product

    list_with_all_prices_men = []
    list_with_all_prices_women = []
    list_with_all_prices_unisex = []
    list_with_all_prices_infant = []
    list_with_all_prices_other = []

    for product in list_of_products:
        single_product_info.append(product.split(','))

    for product_info in single_product_info:
        print(product_info[5])
        list_with_all_prices_men.append(float(product_info[6]))

    return list_with_all_prices_men

def calculate_average_price(prices_of_products): # products is an list of floats
    total_price = 0
    number_of_products = len(prices_of_products)

    for price_product in prices_of_products:
        total_price += price_product
    return total_price/number_of_products

list_of_products = extract_info_in_a_list('./catalog_sample.csv')

prices_of_products = extract_prices_in_a_list(list_of_products)

average = calculate_average_price(prices_of_products)

print(average)

