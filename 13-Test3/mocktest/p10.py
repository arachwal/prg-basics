def f(value1):
    
    def f2(value2):
        return value1 * value2
    return f2

times_five = f(5)
print(times_five(8))