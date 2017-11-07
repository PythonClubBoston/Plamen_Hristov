ftext = input('Please add text: ')
if(len(ftext) == 0 ):
    print('Please add your text')
    ftext = input('Please add text: ')
searchText = input('Please add text2: ')
if(len(searchText) == 0 ):
    print('Please add you text')
    searchText = input('Please add text2: ')
index =  ftext.index(searchText) + len(searchText)
print(ftext[index:])