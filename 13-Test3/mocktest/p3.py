d={"LO231":150,
   "BA787":120,
   "NZ15":30
   }

def f(d):
    number=0
    suma=sum(value for value in d.values())
    avg=suma/len(d)
    for value in d.values():
        if value>avg:
            number+=1
    return number
    

print(f(d))    