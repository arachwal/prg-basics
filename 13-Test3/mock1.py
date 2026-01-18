word='siema'

def f(word):
    name=''
    count=0
    
    for i in range(len(word)):
        for j in range(len(word)):
            if j==count:
                name+=word[j].upper()
            else:
                name+=word[j]
        name+="-"
        count+=1

    return name[:len(name)-1]

print(f(word))