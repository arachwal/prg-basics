def f(amount_to_pay):
    coin5=amount_to_pay//5
    amount_to_pay=amount_to_pay%5
    coin2=amount_to_pay//2
    amount_to_pay=amount_to_pay%2
    coin1=amount_to_pay
    total= coin1+coin2+coin5
    return total

amount_to_pay=23
print(f(amount_to_pay))
    