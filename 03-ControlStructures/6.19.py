'''
Yes-no question are often used in surveys to gauge people's attitudes with regard to specific ideas or beliefs.
Write a program that prints a survey consisting of three questions. Save the answers to logical type variables.
Then view the survey result. Sample result:

SURVEY Are you interested in computer science? (y/n): y
Do you like playing computer games? (y/n): n
Do you have an Instagram account? (y/n): y

SURVEY RESULTS Interested in computer science: Yes
Playing computer games: No
Has an Instagram account: Yes
'''

cs=input('Are you interested in computer science? (y/n): ')
cg=input('Do you like playing computer games? (y/n): ')
ig=input('Do you have an Instagram account? (y/n): ')

if cs == 'y':
    cs='yes'
elif cs =='n':
    cs='no'

if cg == 'y':
    cg='yes'
elif cg =='n':
    cg='no'

if ig == 'y':
    ig='yes'
elif ig =='n':
    ig='no'

print('SURVEY RESULTS ', end="")
print(f'computer science: {cs}')
print(f'computer games: {cg}')
print(f'instagram: {ig}')


