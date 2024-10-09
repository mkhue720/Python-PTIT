n = int(input())
for i in range(n):
    N = input()
    tich = 1
    for t in N:
        if t != '0':
            tich *= int(t)
    print(tich)