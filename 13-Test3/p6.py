res=[95,90,20,50,70]
fnc1= lambda x: x>50
fnc2=lambda x: x>30 and x<90

def f(fnc,res):
    resafter=[]
    for x in res:
        if fnc(x):
            resafter.append(x)
    return max(resafter)+min(resafter)

print(f(fnc1,res))

    