# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender=''

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.gender='Male'
    student2.name = "Olivia"
    student2.age = 21
    student2.gender='Female'
    student3.name='google'
    student3.age= 67
    student3.gender='gmail'

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name},gender: {student1.gender},age: {student1.age} years old')
    print(f'{student2.name},gender: {student2.gender},age: {student2.age} years old')
    print(f'{student3.name},gender: {student3.gender},age: {student3.age} years old')

if __name__ == "__main__":
    main()