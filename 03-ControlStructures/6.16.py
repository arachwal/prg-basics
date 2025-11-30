'''
A washing machine allows you to wash a jacket, which takes 40 minutes, wash underwear, which takes 70 minutes, and wash shoes, which takes 20 minutes.
In addition, it is possible to program an additional rinse (15 minutes) and an additional spin (9 minutes). The washing machine settings are saved in variables.
Write a program that calculates and prints the total washing time. Sample result:

washing_product = "shoes"
rinse = True
spin = False
Total washing time: 35 minutes

###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')
...
'''

total_washing_time = 0

# Get user input for washing item and extra options
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:').lower()
extra_rinse = input('Extra rinse? (y/n)').lower()
extra_spin = input('Extra spin? (y/n)').lower()

# 1. Determine the base washing time
if program == 'j':
    washing_product = "jacket"
    total_washing_time += 40
elif program == 'u':
    washing_product = "underwear"
    total_washing_time += 70
elif program == 's':
    washing_product = "shoes"
    total_washing_time += 20
else:
    # Handle invalid input for the program selection
    print("Invalid program selection. Defaulting to 0 minutes for wash.")
    washing_product = "Unknown Item"

# 2. Add time for extra rinse
if extra_rinse == 'y':
    total_washing_time += 15
    rinse = True
else:
    rinse = False

# 3. Add time for extra spin
if extra_spin == 'y':
    total_washing_time += 9
    spin = True
else:
    spin = False

# 4. Print the result in the required format
print("washing_product =", '"' + washing_product + '"')
print("rinse =", rinse)
print("spin =", spin)
print("Total washing time:", total_washing_time, "minutes")
