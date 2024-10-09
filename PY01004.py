import math
def check(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
def dem(N):
    count = 0
    for i in range(1, N):
        if math.gcd(i, N) == 1: 
            count += 1
    return count
T = int(input())
for _ in range(T):
    N = int(input()) 
    K = dem(N)  
    if check(K):
        print("YES")
    else:
        print("NO")