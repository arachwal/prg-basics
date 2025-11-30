def f(n):
    primes=[]
    found=0
    number=2
    while found<n:
        for i in range(2,number):
            if number%i==0:
                break
        else:
            primes.append(number)
            found+=1
        number+=1
    return primes[n-1]

print(f(4))
