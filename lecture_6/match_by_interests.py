
people = [
    {
        'name': "Мария",
        'interests': ['пътуване', 'танци', 'плуване', 'кино'],
        'age': 24,
        'gender': "female",
        "ex": ["Кирил", "Петър"],
    },
    {
        'name': "Диана",
        'interests': ['мода', 'спортна стрелба', 'четене', 'скандинавска поезия'],
        'age': 21,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Дарина",
        'interests': ['танци', 'покер', 'история', 'софтуер'],
        'age': 34,
        'gender': "female",
        "ex": ["Борис"],
    },
    {
        'name': "Лилия",
        'interests': ['покер', 'автомобили', 'танци', 'кино'],
        'age': 36,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Галя",
        'interests': ['пътуване', 'автомобили', 'плуване', 'баскетбол'],
        'age': 18,
        'gender': "female",
        "ex": ['Димитър'],
    },
    {
        'name': "Валерия",
        'interests': ['плуване', 'покер', 'наука', 'скандинавска поезия'],
        'age': 27,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Ина",
        'interests': ['кино', 'лов със соколи', 'пътуване', 'мода'],
        'age': 20,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Кирил",
        'interests': ['баскетбол', 'автомобили', 'кино', 'наука'],
        'age': 19,
        'gender': "male",
        'ex': ["Мария"],
    },
    {
        'name': "Георги",
        'interests': ['автомобили', 'футбол', 'плуване', 'танци'],
        'age': 32,
        'gender': "male",
        'ex': [],
    },
    {
        'name': "Андрей",
        'interests': ['футбол', 'скандинавска поезия', 'история', 'танци'],
        'age': 26,
        'gender': "male",
        'ex': ["Мария"],
    },
    {
        'name': "Емил",
        'interests': ['летене', 'баскетбол', 'софтуер', 'наука'],
        'age': 34,
        'gender': "male",
        'ex': ['Дарина'],
    },
    {
        'name': "Димитър",
        'interests': ['футбол', 'лов със соколи', 'автомобили', 'баскетбол'],
        'age': 22,
        'gender': "male",
        'ex': ['Галя'],
    },
    {
        'name': "Петър",
        'interests': ['пътуване', 'покер', 'баскетбол', 'лов със соколи'],
        'age': 23,
        'gender': "male",
        'ex': ["Мария"],
    },
    {
        'name': "Калоян",
        'interests': ['кино', 'покер', 'пътуване', 'автомобили'],
        'age': 29,
        'gender': "male",
        'ex': [],
    },
]

from pprint import pprint
import itertools
#
# print([
#     (p1['name'], p2['name'])
#     for p1, p2 in itertools.combinations(people, 2)
#     if p1['gender'] != p2['gender'] and set(p1['interests']) & set(p2['interests'])
# ])

# help(itertools)
help(itertools.count)
numbers = [1,2,3,4,4,5,1,1,1,1]
names = [ 'Дарина', 'Лилия', 'Галя', 'Дани', 'Дени' ]



# sorted_people = sorted(people, key=lambda p: (p['name'], p['gender']))
# print([person['name'] for person in people])

#names entered by the user

# names = [ 'Дарина', 'Лилия', 'Галя', '']
#
# all_non_empty = True
#
# for n in names:
#     if not n:
#         all_non_empty = False
#         break
# print("All are non-empty: ", all_non_empty)
#
# if all(names):
#     print("OK")
# else:
#     print("Empty names are not allowed")

# names1 = ["","","",""]
#
# if any(names1):
#     print("OK")
# else:
#     print("All names are empty")

# names_started_with_D = []
# for name in names:
#
#     if name.startswith('Д'):
#         names_started_with_D.append(name)
# print(names_started_with_D)

#-----------THE SAME WITH THE ABOVE

# names_filtred = list(filter(lambda n: n.startswith('Д'), names))
# print(names_filtred)

# names_for_birthday_card = []
# for n in filter(lambda n: n.startswith('Д'), names):
#     names_for_birthday_card.append(n)
#     if len(names_for_birthday_card) >= 2:
#         break