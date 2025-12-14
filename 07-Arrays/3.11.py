arr=[1,7,4,11,92,13,15]

'''def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubblesort(arr))'''

sorted=sorted(arr)

print(sorted)