"""

Напишете програма, която търси за файлове във Вашата файлова система. Програмата трябва да получава два параметъра при извикването - къде да търси, и какво да търси. Примерно извикване на програмата:

python3  find.py  /home/user/Downloads  me.jpg
В този случай find.py е името на скрипта, /home/user/Downloads в коя папка да се търси, и me.jpg е името на търсения файл.

Търсенето трябва да да включва всички поддиректории, които се намират в началната директория за търсене.

Ако файлът не е намерен, трябва да се показва съобщение, че файлът не е намерен. В противен случай трябва да се отпечата пълния път до файла.

Ако има повече от един файл със същото име в различни директории трябва да се покаже списък с всички намерени файлове.

Ако сте готови с решението на задачата, можете да направите програмата малко по-полезна, като реализирате възможност да търсите с прост wild card * - в началото или в края на името.

Пример:

python3   find.py   /home/Downloads   me*
В примера по-горе кодът ще трябва да намери всички файлове, чието име започва с me, без значение какви символи следват след това.


"""
from sys import argv
from os import walk, path

def find_file(start_directory: str, file_name: str):

    paths = []

    if file_name.endswith("*"):
        file_name = file_name[:-1]  # remove the * from the file name

        for dirpath, _, filenames_list in walk(start_directory):

            for file in filenames_list:

                if file.startswith(file_name):

                    path_to_file = path.join(dirpath, file)
                    paths.append(path_to_file)

    else:
        for dirpath, _, filenames_list in walk(start_directory):

            if file_name in filenames_list:
                path_to_file = path.join(dirpath, file_name)

                paths.append(path_to_file)

    return paths


filesfound = find_file( './', 'Задача: 2. Намерете времето с най-големи продажби*')
print ()
if len(filesfound):
    for each_file in filesfound:
        print ( "This file was located -->", each_file)
else:
    print (None , "was found. Please try again!")