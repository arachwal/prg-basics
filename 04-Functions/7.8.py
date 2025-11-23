'''
The vending machine accepts 1, 2 and 5 PLN coins. Define a function f(amount_to_pay) that returns the minimum number
of coins that can be used to pay for the purchased product. 
Sample result:

f(23) returns 6
f(8) returns 3
f(2) returns 1
f(0) returns 0
'''


def f(total):

    coin5=total//5
    total=total%5

    coin2=total//2
    total=total%2

    coin1=total

    amount_of_coins=coin5+coin2+coin1

    return amount_of_coins

total=8
print(f(total))