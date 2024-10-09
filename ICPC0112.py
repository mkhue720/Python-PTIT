import math
def check(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def check_triplet(x):
    dem = 0
    for i in range(2, x - 6):
        if check(i) and check(i + 2) and check(i + 6):
            dem += 1
        elif check(i) and check(i + 4) and check(i + 6):
            dem += 1
    return dem

N = int(input())
for _ in range(N):
    n = int(input())
    dem = check_triplet(n)
    print(dem)