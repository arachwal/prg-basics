def f(firstletter,lastletter):
    count=0
    with open('data.txt','r',encoding='utf-8') as file:
        for line in file:
            words= line.split()
            for word in words:
                clean=word.strip(".,!?;:").lower()
                if clean.startswith(firstletter.lower()) and clean.endswith(lastletter.lower()):
                    count+=1
        return count

firstletter='w'
lastletter='d'
    
print(f(firstletter,lastletter))