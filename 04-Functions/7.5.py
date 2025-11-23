'''
In a separate module, define a function that checks if the number is within the range <x, y>.
The function returns a boolean value. Then, create a program and use the function you defined. Sample result:

A number: 7
Number 7 in the range <2,15>: yes
'''

def number_in_range(n):
    range_min=2
    range_max=15
    if n<=range_max and n>=range_min:
        return True
    else: 
        return False
    
n=int(input('number: '))
print(number_in_range(n))