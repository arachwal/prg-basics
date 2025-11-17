'''
Write a program that calculates a dog's age in dog's years. 
For the first two years, a dog's life is equal to 10.5 human 
years. After that, each dog year is equal to 4 human years. 

Sample result:
Enter the dog's age in human years: 15
The dog's age in dog's years is 73 years.
'''

human_years=input("enter dog age in human years: ")
dog_years=0

for i in range(int(human_years)):
    if i<=2:
        dog_years+=10.5
    else:
        dog_years+=4    

print(f"dog is {dog_years} old")

