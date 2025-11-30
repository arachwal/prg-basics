x=2
y=8

def f(x,y):
    sum=0
    for digit in range(x,y):
        is_even=digit%2==0
        if is_even==True and digit<0:
            sum+=1
    return sum

print(f(x,y))
