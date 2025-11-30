code='1114'

def f(code):
    sumofthree=int(code[0])+int(code[1])+int(code[2])
    if sumofthree%7==int(code[3]):
        return True
    return False
    
print(f(code))