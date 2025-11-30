'''
Write a program that converts a decimal number into a binary number. To convert a decimal number to binary, follow these steps:

Read a decimal number from the keyboard.
Divide the number by 2 and note the remainder.
Divide the quotient obtained by 2 and note the remainder.
Repeat the same process till we get 0 as the quotient.
Write the values of all the remainders starting from the bottom to the top. That will be the required binary number.
Sample result:

Enter decimal number: 12
12(10) = 1100(2)
'''

dec=int(input('enter a decimal number: '))
bin=[]

while dec>0:
    r=dec%2
    bin.append(r)
    dec=dec//2

bin.reverse()
bin="".join(map(str, bin))
print(bin)


