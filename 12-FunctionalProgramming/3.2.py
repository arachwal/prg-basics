sentence = 'i completely agree with you'
split=sentence.split()
result = list(map(lambda x:len(x) , split))
print(f'for sentence: {sentence}')
print(f'number of letters in words: {result}')