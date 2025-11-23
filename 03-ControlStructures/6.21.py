'''
There are coins of 1, 2 and 5 Polish Zlotys (PLN). Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.

Enter the amount in PLN: 18
The amount of PLN 18 in coins:
5 PLN coins: 3
2 PLN coins: 1
1 PLN coins: 1
'''

total=18

coin5=total//5
total=total%5

coin2=total//2
total=total%2

coin1=total

print(f'you need {coin5} 5plns, {coin2} 2plns and {coin1} 1plns')        