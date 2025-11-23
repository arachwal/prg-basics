'''
Define the function f(n1,n2,n3), which returns True if at least one of the numbers n1,n2,n3 is negative or False otherwise. Sample result:

f(11,6,-4) returns True
f(5,4,14) returns False
'''

def f(n1,n2,n3):
    
    for number in (n1,n2,n3):
        is_negative=number<0
        if is_negative is True:
            return True
    return False
        
n1=111
n2=6
n3=-4
print(f(n1,n2,n3))