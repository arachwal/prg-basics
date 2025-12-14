import json

def f(age, course, average_grade):
    count=0
    with open('data.json', 'r', encoding='utf-8') as file:
        data=json.load(file)
        for student in data:
            if student.get('age')>=age:
                studies=student.get('studies')
                courses=studies.get('courses')
                for c in courses:
                    name=c.get('name')
                    grades=c.get('grades')
                    if name==course and sum(grades)/len(grades)>=average_grade:
                        count+=1
                        break
    return count


print(f(21,'statistics',4))
