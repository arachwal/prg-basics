sentence='An apple a day keeps the doctor away'
splitted=sentence.split()
print(f'number of words: {len(splitted)}') 

sorted1=sorted(splitted,key=len,reverse=True)
print(sorted1)

sorted2=sorted(splitted)
print(f'alphabetically: {sorted2}')