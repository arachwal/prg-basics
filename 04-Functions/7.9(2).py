number=3124
even=False

def f(number,even):
    sum=0
    number=str(number)
    for digit in number:
        digit=int(digit)
        is_even=digit%2==0
        if is_even==True and even==True:
            sum=sum+digit
        elif is_even==False and even==False:
            sum=sum+digit
    return sum

print(f(number,even))
