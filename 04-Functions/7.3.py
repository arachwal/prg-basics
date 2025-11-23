'''
Each month of a calendar year can be expressed by its name or by a number that indicates the position of the month in year.
In a separate module, define a function month(n) that returns a month name based on the month number (values from 1 to 12).
Then, write a program to print the name of the month 7. Import the module with the created function. Sample result:

Enter month number: 9
The name of month 9 is September
'''

def month(n):
    months=[
        " ",#placeholder for index 0
        "January", 
        "February", 
        "March", 
        "April", 
        "May", 
        "June", 
        "July", 
        "August", 
        "September", 
        "October", 
        "November", 
        "December"
    ]
    if n>=1 and n<=12:
        return months[n]
    else:
        return "invalid month number"
    
n=int(input("give month number: "))
print('the month is: ',month(n))