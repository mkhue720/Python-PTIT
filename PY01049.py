import math
def check(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def check_digit(x):
    n = str(x)
    dem = 0
    for i in n:
        if check(int(i)):
            dem += 1
    return dem

N = int(input())
for _ in range(N):
    n = input()
    dem1 = check_digit(n)
    dem2 = len(n) - dem1
    if check(len(n)) and dem1 > dem2:
        print("YES")
    else:
        print("NO")