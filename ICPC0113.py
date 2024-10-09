import math
def check(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def check_emirp(n, N):
    if not check(n):
        return False
    sodao = int(str(n)[::-1])
    if sodao != n and check(sodao) and sodao < N:
        return True
    return False

T = int(input())

for _ in range(T):
    N = int(input())
    arr = []
    seen = set() 
    for i in range(10, N):
        if i not in seen and check_emirp(i, N):
            sodao = int(str(i)[::-1])
            arr.append((i, sodao))
            seen.add(i)
            seen.add(sodao)
    
    for pair in arr:
        print(pair[0], pair[1], end="  ")
    print()
