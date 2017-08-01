"""

1 - Модули
Python файл се нарича 'module'. Дефинираните в него функции, класове и променливи можете да използвате с import.

Ако имаме Python module utils_module.py в същата директория, както и програмата, която стартираме - program.py:

https://stackoverflow.com/questions/4383571/importing-files-from-different-folder  - Importing files from different folder
https://stackoverflow.com/questions/10095037/why-use-sys-path-appendpath-instead-of-sys-path-insert1-path


"""




from lecture_3 import takovata
import os

celsius_july_31_2017_9pm_watertown = takovata.convert_farenheit_to_celsius(73)

print(celsius_july_31_2017_9pm_watertown)

print(os.path.exists('/home'))

print(os.path.join('home', 'plamen'))

print(os.path.dirname('/home/plamen/PycharmProjects'))

print(os.path.getsize('/home/plamen/PycharmProjects'))

print(os.path.isfile('/home/plamen/PycharmProjects/lecture_1/takovata.txt'))

print(os.path.isdir('/home/plamen/PycharmProjects/lecture_1'))

print(os.path.split('/home/plamen/PycharmProjects/lecture_1/takovata.txt'))

import sys
print("Параметри на програмата:")
print(sys.argv)
for idx, a in enumerate(sys.argv):
    print(idx)
    print(a)


for _, _, filenames in os.walk('./'):
    print("Files in the current dir: ", filenames)
    print("-" * 100)

for _, dirnames, filename in os.walk('../'):
    for dirname in dirnames:
        print(dirname)
        print(filename)
