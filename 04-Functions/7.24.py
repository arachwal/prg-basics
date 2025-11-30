def f(expression):
    i=1
    result=int(expression[0])
    while i<len(expression):
        if expression[i]=='+':
            result=result+int(expression[i+1])
        elif expression[i]=='-':
            result=result-int(expression[i+1])
        i=i+2
    return result

expression='2+9'
print(f(expression))

