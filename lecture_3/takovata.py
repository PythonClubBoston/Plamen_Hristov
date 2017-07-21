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


""" - 4 Parameters with value by default

def bigger(param1, param2 = 23):
    if param1 > param2:
        return param1
    return  param2
result = bigger(34)
print(result)

"""

""" - 5 Named parameters as tuple

"""

def send_email(subject, body,  from_email, to_email, cc_email, attachments):
    print(subject)
    print(body)
    print(from_email)
    print(to_email)
    print(cc_email)
    print(attachments)

send_email(

    subject='What is your name and what it means?',
    body = """
    My name is Plamen Hristov, What is your name '
and what it means? I am from Dupnitsa, Bulgaria.
Where are you from? What is your name and what it means? \n""",
    from_email='from_email: plamen.hristov@ymail.com',
    to_email='to_email: paxi@mail.bg',
    cc_email='cc_email: paxhristov@yahoo.com',
    attachments=None

)


