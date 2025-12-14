x=3
y=5

def create(x,y):
    arr=[[0 for i in range(y)] for i in range(x)]
    return arr

arr=create(x,y)

for row in arr:
    print(row)