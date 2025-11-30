def f(n):
    tab=[]
    for i in range(1,n+1):
        tab.append(i)
    tab="".join(map(str,tab))    
    return tab
    
    
print(f(4))

