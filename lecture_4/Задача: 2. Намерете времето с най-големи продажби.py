"""
Вие сте собственик на online магазин, и искате да проверите в кои дни и часове има най-много продажби. Най-много продажби означава сумата на тези продажби, не броят на извършените продажби.

Свалете файла sales.csv, който съдържа 1000 продажби. Файлът е CSV като първата колона е датата и часа на продажбата, втората колона е сумата на продажбата. Файлът не е подреден.

Напишете код, който показва в кой ден е имало най-много продажби като сума от всички продажби за този ден.

Пример: В понеделник е имало продажби за 2000 лева, във вторник за 2345 лева, а в сряда за 897 лева. Денят с най-много продажби е вторник.

Разширение на задачата
Разширете кода си, така че да показва в кой час има най-много продажби. Интересува ни часа, а не деня.

Пример: За целия период между 13:00 и 14:00 е имало продажби за 897 лева, между 14:00 и 15:00 е имало продажби за 456 лева. Между 13:00 и 14:00 е имало повече продажби отколкото между 14:00 и 15:00


"""
from datetime import date, timedelta, time
import iso8601


def import_information_to_dict() -> dict:
    sales_dict = {}
    with open("/home/plamen/PycharmProjects/lecture_4/sales.csv", "r") as sales_file:
        for line in sales_file:
            sale_info = line.split(',')
            date_of_sale = iso8601.parse_date(sale_info[0]).replace(minute=0, second=0, microsecond=0)
            date_of_sale_list = date_of_sale.split(' ')
            print(date_of_sale_list)
            price_of_sale = sale_info[1]

    return sales_dict

sales = import_information_to_dict()

print(date.hour)

