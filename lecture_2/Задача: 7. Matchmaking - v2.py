
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

for person_index, person_A in enumerate(people):

    for person_B in people[person_index:]:


        """

        set_person_interests_A = set(person_A['interests'])
        set_person_interests_B = set(person_B['interests'])

        common_interest = set_person_interests_A.intersection(set_person_interests_B)

        number_of_common_interest = len(common_interest)

        if(number_of_common_interest == 0):
            continue
        set_person_ex_A = set(person_A['ex'])
        set_person_ex_B = set(person_B['ex'])

        if(len(set_person_ex_A) == 0 or len(set_person_ex_B) == 0):

            the_diff_in_years = abs(int(person_A['age']) - int(person_B['age']))
            if (the_diff_in_years >= 6):
                continue
            else:
                print('{} и {} имат общ интерес и той/те са - {} '.format(person_A['name'], person_B['name'], common_interest))

        number_of_common_ex = len(set_person_ex_B.intersection(person_A['name']))

        if(number_of_common_ex > 0):
            continue
        else:

            the_diff_in_years = abs(int(person_A['age']) - int(person_B['age']))

            if(the_diff_in_years >= 6):
                continue

            else:
                print('{} и {} имат общ интерес и той/те са - {} '.format(person_A['name'], person_B['name'], common_interest))

"""
"""

Да разширим предходната задача.
Вече имаме малко повече информация за хората, и искаме да прибавим допълнителни условия към matchmaking-a.
Освен условията досега:
момиченце с момченце; ако сте по-свободомислещи, можете да комбинирате и момченце с момченце, и момиче с момиче
но все пак да има някакво правило :о); трябва да имат поне един общ интерес;
ще имаме и допълнителни условия:
 - разликата в годините не трябва да бъде по-голяма от 6;
 - не бива да комбинирате хора с бившите им партньори - някакси ще се получи неловко :о)
 -Резултатът от програмата също ще трябва да заизглежда малко по-добре:
  Примерен изход: Мария (24) и Калоян (29) ; общи интереси: пътуване, кино
. . .

"""