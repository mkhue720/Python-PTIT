import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N, K = map(int, input().split())
min = 10**(K-1)
max = 10**K
res = []
for i in range(min, max):
    if gcd(i, N) == 1:
        res.append(i)

for i in range(0, len(res), 10):
    print(' '.join(map(str, res[i:i+10])))    
