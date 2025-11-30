def f(name):
    firstletters=''
    for word in name.split():
        firstletters=firstletters+word[0]
    return firstletters

print(f('internet of things'))
        
