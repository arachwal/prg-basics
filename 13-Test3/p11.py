def f(expression):
    stack=[]
    tokens=expression.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in ('-','+'):
            b=stack.pop()
            a=stack.pop()
            if token=='+':
                stack.append(a+b)
            elif token=='-':
                stack.append(a-b)
    return stack[0]

print(f('2 3 4 5 + - +'))
