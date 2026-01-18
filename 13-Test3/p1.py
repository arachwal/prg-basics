def f(expression):
    stack=[]
    tokens=expression.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token=='-' or token=='+':
            b=stack.pop()
            a=stack.pop()
            if token=='+':
                stack.append(a+b)
            else:
                stack.append(a-b)
    return stack[0]

print(f('2 3 4 5 + - +'))



