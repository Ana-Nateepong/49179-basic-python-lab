while True:
    n = int(input())
    if n == 0: break
    if n < 2:
        print(f"{n} not prime")
        continue
    i = 2
    prime = True
    while i * i <= n:
        if n % i == 0:
            prime = False
            break
        i += 1
    print(f"{n} prime" if prime else f"{n} not prime")
