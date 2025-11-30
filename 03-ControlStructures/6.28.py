'''
Write a program that prints the first twenty words of the Fibonacci sequence.
The sequence is defined as follows: the first term is equal to 0, the second is equal to 1, each subsequent term is the sum of the previous two.
Sample result:

0 1 1 2 3 5 8 13 21 34 ...
'''

'''
a = 0  # Represents F(n-2), the second to last term
b = 1  # Represents F(n-1), the last term

# Print the starting message and the first two terms
print(a, end=" ")
print(b, end=" ")

for i in range(2, 20):
    
    # Calculate the next term
    next_term = a + b
    
    # Print the new term
    print(next_term, end=" ")
    
    temp=b
    a=temp
    b=next_term
'''

def f(n):
    vals=[0,1]
    for i in range (2, n+1):
        vals.append(vals[-1]+vals[-2])
    return vals
    

print(f(20))
    
        
        
    

