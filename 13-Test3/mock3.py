d={'LO231':150,"BA787":120,"NZ15":30}

def f(d):
    num=0
    suma=sum(x for x in d.values())
    avg=suma/len(d)
    for x in d.values():
        if x>avg:
            num+=1
    return num

print(f(d))
