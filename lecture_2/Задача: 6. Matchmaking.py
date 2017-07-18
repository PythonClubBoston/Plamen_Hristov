"""
Да си направим програмка за запознанства.
В едно list-че сме си съчинили малко информация за момиченца и момченца.
 От данните, програмата трябва да изведе
резултати кои хора биха си паснали, съгласно следните правила:
момиченце с момченце; ако сте по-свободомислещи, можете да комбинирате и
момченце с момченце, но все пак да има някакво
 правило :о);
трябва да имат поне един общ интерес;
Примерен резултат:

Мария и Георги - общ интерес: плуване
. . .

"""
people = [
    {
        'name': "Мария",
        'interests': ['пътуване', 'танци', 'плуване', 'кино'],
        'gender': "female",
    },
    {
        'name': "Диана",
        'interests': ['мода', 'спортна стрелба', 'четене', 'скандинавска поезия'],
        'gender': "female",
    },
    {
        'name': "Дарина",
        'interests': ['танци', 'покер', 'история', 'софтуер'],
        'gender': "female",
    },
    {
        'name': "Лилия",
        'interests': ['покер', 'автомобили', 'танци', 'кино'],
        'gender': "female",
    },
    {
        'name': "Галя",
        'interests': ['пътуване', 'автомобили', 'плуване', 'баскетбол'],
        'gender': "female",
    },
    {
        'name': "Валерия",
        'interests': ['плуване', 'покер', 'наука', 'скандинавска поезия'],
        'gender': "female",
    },
    {
        'name': "Ина",
        'interests': ['кино', 'лов със соколи', 'пътуване', 'мода'],
        'gender': "female",
    },
    {
        'name': "Кирил",
        'interests': ['баскетбол', 'автомобили', 'кино', 'наука'],
        'gender': "male",
    },
    {
        'name': "Георги",
        'interests': ['автомобили', 'футбол', 'плуване', 'танци'],
        'gender': "male",
    },
    {
        'name': "Андрей",
        'interests': ['футбол', 'скандинавска поезия', 'история', 'танци'],
        'gender': "male",
    },
    {
        'name': "Емил",
        'interests': ['летене', 'баскетбол', 'софтуер', 'наука'],
        'gender': "male",
    },
    {
        'name': "Димитър",
        'interests': ['футбол', 'лов със соколи', 'автомобили', 'баскетбол'],
        'gender': "male",
    },
    {
        'name': "Петър",
        'interests': ['пътуване', 'покер', 'баскетбол', 'лов със соколи'],
        'gender': "male",
    },
    {
        'name': "Калоян",
        'interests': ['история', 'покер', 'пътуване', 'автомобили'],
        'gender': "male",
    },
]

for person_index, person_A in enumerate(people):
    for person_B in people[person_index + 1:]:
        if(person_A['gender'] == person_B['gender']):
            continue
        common_interest = []
        set_person_A = set(person_A['interests']) #cast person_A to set
        set_person_B = set(person_B['interests']) #cast person_B to set
        name_person_A = person_A['name']


        common_interest = set_person_A.intersection(set_person_B) #if interest are the same
        if len(common_interest) > 0:  # if they have mutual interests
            print('{} и {} имат общ интерес и той/те са - {}'.format(person_A['name'], person_B['name'], common_interest))