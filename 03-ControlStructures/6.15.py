'''
EAN-13 (European Article Number) is a barcode for marking goods. The first 3 digits (590) usually indicate goods manufactured in Poland.
Write a program that checks whether the EAN-13 number entered from the keyboard consists of exactly 13 characters (digits).
Print a message if the number is correct. Additionally, only when the article number is correct, print a message when the product was manufactured in Poland.
Sample result:

Enter EAN-13 article number: 5901230094938
Article number is correct
Article manufactured in Poland
'''


articlenumber='5401145904938'
poland='590'

if len(articlenumber) == 13:
    print('it is a viable article number')
    if poland in articlenumber[0:3]:
        print("its polish")