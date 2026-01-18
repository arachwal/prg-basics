'''files=["copy179",'copy15','copy3','copy123','copy9']

def f(files):
    return sorted(
        files,
        key=lambda x: int(''.join(filter(str.isdigit,x)))
    )

print(f(files))'''

# z drugiej gr zadanie sortowanie alfabetycznie formatu pliku: x

def f(files):
    return sorted(
        files,
        key= lambda x: x.split(".")[-1]
    )

files=['a.txt','b.pdf','ccc.py','ddddd.jpg4']
print(f(files))