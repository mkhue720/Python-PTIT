import math

def check_snt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    c = math.gcd(a, b)
    S = 0
    for i in str(c):
        S += int(i)
    if not check_snt(S):
        print('NO')
    else:
        print('YES')
