cars = [
    {"KR333": 138},
    {"WL555": 497},
    {"DB444": 341},
    {"MC222": 412}
]

def f(cars,order):
    if order==1:
        return sorted(
            cars,
            key=lambda x: list(x.keys())
            )
    
    elif order==2:
        filtered=[x for x in cars if list(x.values())[0]>=200]
        return sorted(
            filtered,
            key=lambda x: list(x.values()),
            reverse=True
            )
    
print(f(cars,2))