arr1=[1,2,3]
arr2=[1,4,2,5,3,6]

subset=True

for element in arr1:
    if element not in arr2:
        subset=False
        break

print(subset)