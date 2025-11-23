meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            }
for i in range(5):
    word = input("Wpisz słowo, którego nie rozumiesz: ").upper()
    
    if word in meme_dict.keys():
        print('Te słowo jest w słowniku i oznacza ono:')
        print(meme_dict[word])
    else:
        for i in range(5):
            print('Nie ma tego słowa, możesz je dodać')
            head = input('Wpisz jakie słowo dodajesz:')
            body = input('Wpisz jego znaczenie:')
            meme_dict[head]=body
            print('Dodano nowe słowo do słownika!')
            print(head, ':', body)
