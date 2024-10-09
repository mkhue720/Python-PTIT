def tich(x):
    T = 1
    for i in str(x):
            T *= int(i)
    return T
N = int(input())

for i in range(N):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(key=lambda x: (tich(x), x))
    print(" ".join(map(str, A)))
