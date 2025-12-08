# takes two numbers from keyboard
n1 = int(input('numer1; '))
n2 = int(input('numer2; '))

# define an anonymous function
mean = lambda x,y: (x+y)/2


# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f"The arithmetic mean of {n1}+{n2}/2 is {result}")