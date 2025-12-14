import csv

def f(value):
    count=0

    with open('data.csv','r',encoding='utf-8') as file:
        data=csv.DictReader(file)
        for row in data:
            salary=int(row['salary'])
            if salary>=value:
                count+=1
    return count

print(f(5200))
