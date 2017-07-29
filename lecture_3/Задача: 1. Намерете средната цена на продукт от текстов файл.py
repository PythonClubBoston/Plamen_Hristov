"""

Свалете тези два файла (catalog_sample.csv) и (catalog_full.csv)
 Файловете са реален продуктов каталог на на известен производител на спортни стоки, с описание и цени
 (цените са произволни), като разликата между двата файла е в броя на артикулите. catalog_sample има само 200 артикула,
 докато catalog_full има над 60000. Структурата на двата файла е еднаква.

catalog_sample.csv

catalog_full.csv

Напишете програма, която намира средната цена от всички артикули във файла.

Структурата на CSV файловете е следната:
1. каталожен номер
2. име на продукта
3. цветове на продукта.
4. Ако са повече от един са разделени с /за какъв вид
5. активност е предназначен артикула
6. каква е групата на артикула за
7. кой пол и възраст е предназначен артикула
8. цена
Разделителят на данните е , (запетая), а десетичният знак е . (точка)

"""

def extract_info_in_a_list(path_to_info_as_string): # return list with the info for the products
    with open(path_to_info_as_string, 'r') as catalog_with_products:
        catalog_list_with_products = []

        for line in catalog_with_products:
            #https://stackoverflow.com/questions/3849509/how-to-remove-n-from-a-list-element
            catalog_list_with_products.append(line.strip())

        return catalog_list_with_products

def extract_prices_in_a_list(list_of_products): #return list with prices of the product
    single_product_info = []
    list_with_all_prices = []

    for product in list_of_products:
        single_product_info.append(product.split(','))

    for product_info in single_product_info:
            list_with_all_prices.append(float(product_info[6]))

    return list_with_all_prices

def calculate_average_price(prices_of_products): # products is an list of floats
    total_price = 0
    number_of_products = len(prices_of_products)

    for price_product in prices_of_products:
        total_price += price_product
    return total_price/number_of_products

list_of_products = extract_info_in_a_list('./catalog_full.csv')
print(len(list_of_products))
prices_of_products = extract_prices_in_a_list(list_of_products)

average = calculate_average_price(prices_of_products)

print(average)