'''
Define the function f(x,y) that returns the number of negative even numbers in the range <x,y>. Sample result:

f(-7,8) returns 3
f(-1,11) returns 0
'''

def f(x,y):
    number_of_numbers=0
    
    for digit in range(x,y):
        is_even=digit%2==0
        is_negative=digit<0
        if is_even == True and is_negative == True:
            number_of_numbers+=1
    return number_of_numbers
x=-1
y=11
print(f(x,y))
