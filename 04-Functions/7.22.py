name ='internet of things'

def f(name):
    firstletters=""
    for word in name.split():
        firstletters+=word[0]
    return firstletters

print(f(name))