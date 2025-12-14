'''arr=[1,1,2,2,3,3,3,4,4,5,5,5,5]

counts={}
for i in arr:
    if i in counts:
        counts[i]+=1
    else:
        counts[i]=1

for key,value in counts.items():
    if value%2==1:
        print(value)'''

print(sum(i for i in range(5)))
