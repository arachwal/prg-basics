###
# Calculates the total value of money spent
#
import re # module for regular expressions

# read the content of email
with open('report.txt', 'r') as file:
   email = file.read()

# regular expression pattern
# for amounts
pattern = '\d'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)
print(amounts)

# calculate the total purchases
...
for amount in amounts:
   ...

# print result
print(...)