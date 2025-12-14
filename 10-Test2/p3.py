arr=[
    [3,7,2],
    [4,2,5],
    [9,2,1]
    ]

def f(arr):
    row1=sum(arr[0]) #sum of values in rows
    row2=sum(arr[1])
    row3=sum(arr[2])

    column1=sum(row[0] for row in arr) #sum of values in columns
    column2=sum(row[1] for row in arr)
    column3=sum(row[2] for row in arr)

    if row1==column1 and row2==column2 and row3==column3:
        return True
    else:
        return False
    

print(f(arr))