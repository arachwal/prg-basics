###
# Calculates the total value of money spent
#
import re # module for regular expressions

<<<<<<< HEAD
# file name with shopping report
email_file = 'report.txt'

# read the content of email
...
...
email = ... (email content)

# regular expression pattern
# for amounts
pattern = '....'
=======
# read the content of email
with open('report.txt', 'r') as file:
   email = file.read()

# regular expression pattern
# for amounts
pattern = '\d'
>>>>>>> d921c6b5b0ca16f1d076142980790a72668856bb

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)
<<<<<<< HEAD
=======
print(amounts)
>>>>>>> d921c6b5b0ca16f1d076142980790a72668856bb

# calculate the total purchases
...
for amount in amounts:
   ...

# print result
print(...)