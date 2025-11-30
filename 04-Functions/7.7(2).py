def f(binary_number):
    numbers=['0','1']
    for digit in binary_number:
        if digit not in numbers:
            return False
    return True
    
binary_number='10101011'
print(f(binary_number))