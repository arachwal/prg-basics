arr = [7,9,2,4,5,6]
parzyste=[]
nieparzyste=[]

for i in arr:
    if i%2==0:
        parzyste.append(i)
    else:
        nieparzyste.append(i)


sort=parzyste+nieparzyste
print(sort)
