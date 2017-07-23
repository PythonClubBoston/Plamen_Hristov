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

product_catalog_number = 0
product_name = ''
product_color = ''
product_group = ''
product_activity = ''
product_price = 0.00
product_gender_purpose = ''

def extract_info_in_a_list(path_to_info_as_string): # return list with the info for the product
    with open(path_to_info_as_string, 'r') as sample_catalog:
        sample_catalog_list = []
        for line in sample_catalog:
            #https://stackoverflow.com/questions/3849509/how-to-remove-n-from-a-list-element
            sample_catalog_list.append(line.strip())
        return sample_catalog_list

list_of_products = extract_info_in_a_list('./catalog_sample.csv')
print(list_of_products)

products = ['10117,GRAND TOUR II,RUNNINWHT/NEW NAVY,TENNIS,SHOES,Men,691.99', 'GRAND TOUR II W,RUNNINWHT/PINK.PO.,TENNIS,SHOES,Woman,283.99']

prices_of_products = [691.99, 283.99]

def calculate_average_price(prices_of_products): # products is an list of floats
    total_price = 0
    number_of_products = len(prices_of_products)
    for price_product in prices_of_products:
        total_price += price_product
    return total_price/number_of_products

ave = calculate_average_price(prices_of_products)
print(ave)

