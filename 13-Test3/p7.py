files=["copy179",'copy15','copy3','copy123','copy9']


def f(files):
    return sorted(
        files,
        key=lambda x: int(''.join(filter(str.isdigit,x))))

print(f(files))