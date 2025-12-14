tup=[5,2,4,5,3,5]

'''counts={}
for item in tup:
    if item in counts:
        counts[item]+=1
    else:
        counts[item]=1

for value,counts in counts.items():
    print(f'{value} appears {counts} times')'''

to_count=5
count=tup.count(to_count)
print(count)
