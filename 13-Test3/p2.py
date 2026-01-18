d="+-+++++-"

def f(d):
    num=0
    for sign in d:
        if sign=="+":
            num+=1
        elif sign=="-":
            num-=1
    return num

print(f(d))