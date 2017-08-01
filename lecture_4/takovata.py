"""

1 - Модули
Python файл се нарича 'module'. Дефинираните в него функции, класове и променливи можете да използвате с import.

Ако имаме Python module utils_module.py в същата директория, както и програмата, която стартираме - program.py:

https://stackoverflow.com/questions/4383571/importing-files-from-different-folder  - Importing files from different folder
https://stackoverflow.com/questions/10095037/why-use-sys-path-appendpath-instead-of-sys-path-insert1-path


"""




from lecture_3 import takovata

celsius_july_31_2017_9pm_watertown = takovata.convert_farenheit_to_celsius(73)

print(celsius_july_31_2017_9pm_watertown)
