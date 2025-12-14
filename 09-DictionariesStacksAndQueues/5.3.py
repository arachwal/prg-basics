translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}


user=str(input('word: '))
if user in translations:
    print(translations[user])
else:
    print('nie ma tlumaczenia')
        