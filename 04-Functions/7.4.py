'''
Write a program that calculates how many times the given letter appears in any text.
Then create a program and check how many times the letter 'e' appears in the text below.
In a separate module, define a function for making calculations. Sample result:

You never get a second chance to make a first impression
The number of letter 'e': 7
'''

letters="e"

def calc(letters):
    sentence='You neever get a second chanece to maeke a first impression'
    sum=0
    for letter in sentence:
        if letter in letters:
            sum+=1
    return sum

print(calc(letters))
