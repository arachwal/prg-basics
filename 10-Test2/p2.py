arr=[7,7,7,7,7,5,7,7]
def f(arr):
    common=arr[5]
    for i in arr:
        if i!=common:
            return i
    
print(f(arr))