'''
Write a program that allows you to convert time in 24-hour format to 12-hour format.
The time in 24-hour format (hh:mm) is read from the keyboard. Sample result:

Enter time (24-hour format): 16:32
Time in 12-hour format: 4:32pm
'''

time24=input('enter time in 24h (hh:mm) format: ')
hour, minute = map(int,time24.split(':'))

if hour == 0:
    hour12 = 12
    period="am"
elif hour == 12:
    hour12 = 0
    period = "pm"
elif hour <=11 and hour >=1:
    hour12=hour
    period="am"
else:
    hour12=hour-12
    period="pm"

print(f'{time24} in 12h format is {hour12}:{minute} {period}')