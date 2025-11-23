'''
Write a program that creates the following pattern. Sample result:

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

maxstars=5

for i in range(1,maxstars+1):
    print("* "*i)
for i in range(maxstars-1, 0, -1):
    print("* "*i)

