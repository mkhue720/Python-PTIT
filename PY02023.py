def tong(x):
    return sum(int(so) for so in str(x))
N = int(input())

for i in range(N):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(key=lambda x: (tong(x), x))
    print(" ".join(map(str, A)))
