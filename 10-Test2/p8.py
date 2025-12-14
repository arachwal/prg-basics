def f(expression):
    stack = []
    tokens = expression.split()  # split the string by spaces

    for token in tokens:
        if token.isdigit():       # if token is a number
            stack.append(int(token))
        elif token in ('+', '-'):  # if token is an operator
            b = stack.pop()       # second operand
            a = stack.pop()       # first operand
            if token == '+':
                stack.append(a + b)
            else:
                stack.append(a - b)

    return stack[0]

expression=("2 1 + ")

print(f(expression))