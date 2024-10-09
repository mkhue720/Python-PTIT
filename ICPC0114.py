import math

def check(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def check_digit(N):
    n = str(N)
    for i in n:
        if i not in {'2', '3', '5', '7'}:
            return False
    return True

def sum_digit(N):
    S = 0
    while N > 0:
        S += N % 10
        N //= 10
    return S

N = int(input())
for _ in range(N):
    n = int(input())
    sodao = int(str(n)[::-1])
    if check(n) and check(sodao) and check_digit(n) and check(sum_digit(n)):
        print('Yes')
    else:
        print('No')
