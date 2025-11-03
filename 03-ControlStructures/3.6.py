
# Checks if the given day number of the month is correct


month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the day: '))
day_ok = False


if month%2==1 and month != 11:
    if day >=1 and day <= 31:
        day_ok = True
elif month%2==0 or month==11:
    if day >=1 and day <= 30:
        day_ok = False



if day_ok:
    print('the number of days in that month is correct 😎')
else:
    print('the number of days in that month is NOT correct 🥀')

