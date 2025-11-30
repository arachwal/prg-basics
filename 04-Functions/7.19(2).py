number=230335

from collections import Counter
def f(number):
    snumber=str(number)
    counts=Counter(snumber)
    sum=0
    for digit in snumber:
        if counts[digit]>1:
            sum+=int(digit)
    return sum

print(f(number))

