import math

def output(N, X, M):
    if M <= N:
        return 0
    r = 1 + X / 100
    t = math.ceil(math.log(M / N) / math.log(r))
    
    return t
n = int(input())
for _ in range(n):
    N, X, M = map(float, input().split())
    so_nam = output(N, X, M)
    print(so_nam)
