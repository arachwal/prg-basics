res = [95,90,20,50,70]
fnc2 = lambda x: x>30 and x<90 


def f(res,fnc1):
    arr1=[]
    for x in res:
        if fnc1(x) == True:
            arr1.append(x)
    return max(arr1)-min(arr1)
    
print(f(res,fnc2))