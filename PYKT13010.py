MOD = 10**9 + 7

def tong(n, k):
    if k == 1:
        return (n * (n + 1) // 2) % MOD
    elif k == 2:
        return (n * (n + 1) * (2 * n + 1) // 6) % MOD
    elif k == 3:
        return ((n * (n + 1) // 2) ** 2) % MOD 
    else:
        return sum(pow(i, k, MOD) for i in range(1, n + 1)) % MOD

N = int(input())
for _ in range(N):
    n, k = map(int, input().split())
    print(tong(n, k))
