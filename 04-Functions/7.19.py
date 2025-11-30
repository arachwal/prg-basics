
'''
def f(number):
    snumber=str(number)
    counts=Counter(snumber)
    sum=0
    for digit in snumber:
        if counts[digit]>1:
            sum=sum+int(digit)
    return sum
    
number=239335
print(f(number))
'''
from collections import Counter

def f(number):
    snumber=str(number)
    counts=Counter(snumber)
    sum=0
    for digit in snumber:
        if counts[digit]>1:
            sum+=int(digit)
    return sum

number=239335
print(f(number))
