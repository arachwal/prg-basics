arr=[7,3,8,5,2]

print(','.join(map(str,arr))) #1

sorted=sorted(arr)
second_last=sorted[-2]
print(second_last) #2

n=len(sorted)
if n%2==1:
    median=sorted[n//2]
else:
    median=(sorted[n//2-1]+sorted[n//2])/2
print('median:', median) #3

print(f'smallest and largest number: {sorted[0]}, {sorted[-1]}') #4

print("-".join(map(str,arr))) #5
