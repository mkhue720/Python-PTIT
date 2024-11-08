#TLE
def count(L, R, N):
    dem = 0
    
    for i in range(L, R + 1):
        check = False
        for j in range(2, N + 1):
            if i % j == 0:
                check = True
                break 
        if not check:
            dem += 1 
    return dem

while True:
    n = input()
    if n.strip() == '-1':
        break
    L, R = map(int, n.split())
    N = int(input())
    res = count(L, R, N)
    print(res)
