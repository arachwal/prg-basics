'''def f(n):
    found=0
    number=1
    while found<n:
        number+=1
        prime=True
        if number<2:
            prime=False
        else:
            for i in range(2,number):
                if number%i==0:
                    prime=False
                    break
        if prime:
            found+=1
    return number

print(f(4))'''

def f(n):
    number=2
    found=0
    primes=[]

    while found<n:
        for i in range(2, number):
            if number%i==0:
                break
        else:
            primes.append(number)
            found+=1
        number+=1
    return primes[n-1]

print(f(5))

