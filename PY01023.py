from math import sqrt

for _ in range(int(input())):
    n = int(input())
    sqr = int(sqrt(n))
    check = True 
    print(1, end="")
    for i in range(2, sqr + 1):
        if n % i == 0:
            dem = 0
            while n % i == 0:
                dem += 1
                n //= i
            if check:
                print(f" * {i}^{dem}", end="")
                check = False
            else:
                print(f" * {i}^{dem}", end="")
            sqr = int(sqrt(n))
    if n > 1:
        if check:
            print(f" * {n}^1", end="")
        else:
            print(f" * {n}^1", end="")
    print()
