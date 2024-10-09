import math
def check(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    N = input()
    if len(N) >= 4 and check(int(N[-3:])) and check(int(N[:3])):
        print("YES")
    else:
        print("NO")