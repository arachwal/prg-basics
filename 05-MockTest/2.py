
### The program checks what the temperature is and suggests an action depending on the temperature. Unfortunately,
### the advice does not match the temperature. Modify the program so that it works correctly. Use debugging mode to
### follow the program's statements step by step.


temperature = 1111111  # In Celsius

if temperature > 30:
    print("It's hot outside. Stay hydrated!")
elif temperature > 20:
    print("The weather is nice. How about a walk?")
elif temperature > 10:
    print("It's a bit chilly. You might need a jacket.")
else:
    print("It's cold! Stay indoors or bundle up!")

print('I hope I helped somehow.')