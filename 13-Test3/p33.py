def f(name):
    if len(name)>1 and len(name)<=6:
        if name[0].isalpha() or name[0]=='_':
            for char in name[1:]:
                if not (char.isalpha() or char.isdigit() or char=="_"):
                    return False
                else:
                    return True
        else:
            return False
    else:
        return False
        


name='abdefasfa'
print(f(name))