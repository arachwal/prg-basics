'''
Create a function f(number, even) that computes the sum of the digits of a number.
When the value of the even parameter is True, the function returns the sum of the even digits.
When the value of the even parameter is False, the function returns the sum of the odd digits.
Sample result:

f(3124,True) returns 6
f(3124,False) returns 4
f(20576,False) returns 12
f(20576,True) returns 8
f(13115,True) returns 0
'''

def f(number, even):
    suma=0
    number=str(number)
    
    for digit in number:
        digit=int(digit)
        even_digit = digit%2==0
        if even == True and even_digit == True:
            suma += digit
        if even == False and even_digit == False:
            suma += digit
    return suma

number=13115
even=True
print(f(number,even))
    

