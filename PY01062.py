import math

def check(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

N = int(input())
nto  = {'2', '3', '5', '7'}
for _ in range(N):
    n = input()
    dem1 = 0
    dem2 = 0
    for i in n:
        if i in nto:
            dem1 += 1
        else:
            dem2 += 1
    if check(len(n)) and dem1 > dem2:
        print('YES')
    else:
        print('NO')