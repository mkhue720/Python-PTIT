# TLE
import math
def check(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

N = int(input())
for _ in range(N):
    n = int(input())
    for i in range(n+1, n+10):
        if not check(i):
            print(i)
            break