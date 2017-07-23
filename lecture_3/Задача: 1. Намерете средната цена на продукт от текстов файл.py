"""

Свалете тези два файла (catalog_sample.csv) и (catalog_full.csv)
 Файловете са реален продуктов каталог на на известен производител на спортни стоки, с описание и цени
 (цените са произволни), като разликата между двата файла е в броя на артикулите. catalog_sample има само 200 артикула,
 докато catalog_full има над 60000. Структурата на двата файла е еднаква.

catalog_sample.csv

catalog_full.csv

Напишете програма, която намира средната цена от всички артикули във файла.

Структурата на CSV файловете е следната:

каталожен номер
име на продукта
цветове на продукта. Ако са повече от един са разделени с /
за какъв вид активност е предназначен артикула
каква е групата на артикула
за кой пол и възраст е предназначен артикула
цена
Разделителят на данните е , (запетая), а десетичният знак е . (точка)


"""

products = ['10117,GRAND TOUR II,RUNNINWHT/NEW NAVY,TENNIS,SHOES,Men,691.99', 10120, 'GRAND TOUR II W,RUNNINWHT/PINK.PO.,TENNIS,SHOES,Woman,283.99']

prices_of_products = [691.99, 283.99]

def averagePrice(prices_of_products): # products is an list of floats
    total_price = 0
    number_of_products = len(prices_of_products)
    for price_product in prices_of_products:
        total_price += price_product
    return total_price/number_of_products

ave = averagePrice(prices_of_products)
print(ave)