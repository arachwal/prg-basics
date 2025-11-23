'''
Write a program that creates the following pattern. Sample result:

1
22
333
4444
55555
666666
7777777
88888888
999999999
'''

number=9

for i in range(1,number+1):
    print(f"{i} "*i)
