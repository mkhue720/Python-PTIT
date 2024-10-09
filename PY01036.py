n = int(input())
while n > 0 :
    N = int(input())
    S = 0
    if N % 2 != 0 :
        for i in range(1, N+1, 2) :
            S += 1 / i
    else :
        for i in range(2, N+1, 2) :
            S += 1 / i
    print("{:.6f}".format(S))
    n -= 1