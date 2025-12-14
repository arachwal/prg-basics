para="cat dog mouse cat rat cat mouse"
words=para.split()
dictionary={}
for word in words:
    if word in dictionary:
        dictionary[word]+=1
    else:
        dictionary[word]=1
print(dictionary)