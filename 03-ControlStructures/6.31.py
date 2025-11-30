'''Write a program that prints 20 integer random numbers in the range of 5 to 10.'''

import random
numss=[]

for _ in range(20):
    print(random.randint(5, 10), end="")

'''
for i in range(20):
    nums=random.randint(5,10)
    numss.append(nums)

numss="".join(map(str, numss)) !!!!!
print(numss)
'''