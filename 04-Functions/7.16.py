def f(n):
    vals=[0,1]
    for i in range(2,n+1):
        vals.append(vals[-1]+vals[-2])
    return vals[n-1]

n=5
print(f(n))