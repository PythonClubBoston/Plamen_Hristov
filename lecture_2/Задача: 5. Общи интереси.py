"""
Вие сте създател на популярен сайт за запознанства и искате да улесните вашите потребители да намерят своята
 половинка.
За целта вие събирате информация за интересите на всеки потребител и се опитвате да намерите партньор с
максимално общи
интереси. Имате дадени два списъка които съдържат интересите на Иванчо и Марийка.
Като използвате данните по-долу, копирайте ги в Python програма и допишете код, който показва само
общите интереси между
двамата.
"""

ivan = ['пушене', 'пиене', 'тия три неща', 'коли',
        'facebook', 'игри', 'разходки по плажа', 'скандинавска поезия']
maria = ['пиене', 'мода', 'facebook', 'игри',
         'лов със соколи', 'шопинг', 'кино']




ivan_intrests = set(ivan)
maria_intrests = set(maria)
common_intrests = ivan_intrests.intersection(maria_intrests)
print(common_intrests)


""" 

SECOND WAY
common_intrests = []
for i, value in enumerate(ivan):
    for j, value in enumerate(maria):
        if(ivan[i] == maria[j]):
            common_intrests.append(ivan[i])
print(common_intrests)

"""

""" 

THIRD WAY



"""