def f(n1,n2,operator):
    if operator=="*":
        return n1*n2
    elif operator=="%":
        return n1%n2
    elif operator=="**":
        return n1**n2
    elif operator=="+":
        return n1+n2
    elif operator=="-":
        return n1-n2
n1=2
n2=3
operator="**"
print(f(n1,n2,operator))