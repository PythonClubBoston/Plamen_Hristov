"""

"""

""" - 1

def printTemperature(temp1, temp2):
    print('Temperature outside vary from {} to {} degrees'.format(temp1, temp2))

printTemperature(27, 33)

"""

""" - 2 - functions can return value

def convert_fahrenheit_to_celsius(deg_f):
    celsius =  (deg_f - 32) / 1.8
    return celsius

returned_value = convert_fahrenheit_to_celsius(34)
print(returned_value)

"""

""" - 3 Return few things from function in tuple format

def div_mode(number, divisor):
    result = number / divisor
    modulus = number % divisor
    return (result, modulus)

tuple_result = div_mode(43, 17)

a, b = tuple_result
print(a)
print(b)

"""


""" - 4 Parameters with value by default always
        after the parameters without default value

def bigger(param1, param2 = 23):
    if param1 > param2:
        return param1
    return  param2
result = bigger(34)
print(result)

"""

""" - 5 Named parameters and required

def send_email(subject, body,  from_email, to_email, cc_email, attachments):
    print(subject)
    print(body)
    print(from_email)
    print(to_email)
    print(cc_email)
    print(attachments)

send_email(

    subject='What is your name and what it means?',
    body =     
   'My name is Plamen Hristov, What is your name ' +
'and what it means? I am from Dupnitsa, Bulgaria.' +
'Where are you from? What is your name and what it means? \n',
    from_email='from_email: plamen.hristov@ymail.com',
    to_email='to_email: paxi@mail.bg',
    cc_email='cc_email: paxhristov@yahoo.com',
    attachments=None

)
"""

""" - 6 Functions with number of argumentes *arg 
def sum_numbers(*args): # the name of the args is optional
#we can use for examples instead *args -> *options, *args is smth like convetion
    total = 0
    for n in args:
        total += n
    return total

result1 = sum_numbers(1,2)
result2 = sum_numbers(1,2,3)
result3 = sum_numbers(1,2,3,4)
result4 = sum_numbers(1,2,3,4,5)
print(result1)
print(result2)
print(result3)
print(result4)

print(result1 + result2 + result3 + result4)

"""

""" - 7 Functions with number of argumentes **kwards

def pretty_print_record(**kwargs): # kwards will be a regular dictionary
    print("Record:")
    for key, value in kwargs.items():
        print("\t", key, "= ", value)
pretty_print_record(name="Plamen", distance_au = 23.34, diameter = 222)

"""

""" - 8 Call functions with *args and **kwargs
def format_with_indent(format_string, *args, indent: int=None, indent_with: str=" ", **kwargs):
    if indent is not None:
        indent_str = indent_with * indent  # will multiply the indent string
    else:
        indent_str = ""
    return indent_str + format_string.format(*args, **kwargs)

...

print(format_with_indent("Name: {}, Role: {role}", 'Boris', role='lecturer'))    

print(format_with_indent("Name: {}, Role: {role}", 'Boris', role='lecturer', indent=4))    

print(format_with_indent("Name: {}, Role: {role}", 'Boris', role='lecturer', indent=4, indent_with='-'))

"""
""" - 9 Annotaions for parametars and returened type of the value

def convert_fahrenheit_to_celsiusd(deg_f: float): # no errors raised if you placed a wrong type of the data
    return (deg_f - 32)/1.8
result = convert_fahrenheit_to_celsiusd(33.02)
print(type(result))

"""

""" - 10 - Functions in Python are values

def convert_fahrenheit_to_celsiusd(deg_f: float): # no errors raised if you placed a wrong type of the data
    return (deg_f - 32)/1.8

test_function = convert_fahrenheit_to_celsiusd

print(test_function(32))

"""

""" 11 - Functions and Scope of the variables 

def convert_farenheit_to_celsius(degrees_f):
    degrees_c = (degrees_f - 32)/1.8
    return degrees_c
print(convert_farenheit_to_celsius(32))
print(degrees_c)  # error грешка - променливата degrees_c е дефинирана във функцията, и тук не съществува
print(degrees_f)  # error грешка - degrees_f е параметър на функцията, и тук не съществува


"""

""" - 12 Exceptions, raising and process 

people = [{'name': "Мария", 'gender': "female", 'age': 32}, {'name': "Калоян", 'gender': "male", 'age': 33}, ]

...
def print_person(person: dict):
    if 'age' or 'interests' not in person:
        raise ValueError('Ключът "age/interests" са задължителени в параметъри "person"')

    print("{} ({}) is interested in {}".format(
        person['name'],
        person['age'],
        ', '.join(person['interests'])
    ))

def print_people(people: list):
    for person in people:
        print_person(person)

print_people(people)


"""

""" - 13 Working with text files !!!!!!!

#open

salve_mea_lyrics = open('./takovata.txt')
for line in salve_mea_lyrics:
    print(line)
salve_mea_lyrics.close()

#with open

with open('./takovata.txt') as salve_mea_lyrics:
    for line in salve_mea_lyrics:
        print(line)
        
with open('./numbers.txt', 'w') as f:   # с 'w' съдържанието на файла ще бъде изтрито, и ще започнем в пишем на празен файл
    for i in range(20):
        f.write(str(i))
        f.write("\n")

"""

with open('./numbers.txt', 'a') as f:   # с 'а' съдържанието на файла се запази, и писането в този файл ще допълва в края на файла
    for i in range(20):
        f.write(str(i))
        f.write("\n")

"""
Други полезни методи:

.readline() - прочита една линия от отворения файл, като връща str, който включва разделителя за нов ред
.readlines() - прочита всички линии от файла и връща list от str с всички прочетени линии. ако файлът е прекалено голям, с използването на този метод е възможно да заемете прекалено много памет;
.read() - без параметър прочита цялото съдържание на файла, и връща str. ако файлът е прекалено голям, с използването на този метод е възможно да заемете прекалено много памет;
.read(max_chars) - прочита най-много указания брой символи от файла, и връща str

"""