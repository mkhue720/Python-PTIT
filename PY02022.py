def check(N):
    if N < 2:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True

N = int(input())
A = list(map(int, input().split()))
dem = {}

for i in A:
    if check(i):
        if i in dem:
            dem[i] += 1 
        else:
            dem[i] = 1 
for i in dem:
    print(f"{i} {dem[i]}")
