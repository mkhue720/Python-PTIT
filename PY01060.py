n = int(input())
for i in range(n):
    N = input()
    tich = 1
    tong = 0
    check = False
    for t in range(len(N)):
        chu_so = int(N[t])
        if t % 2 != 0:
            tong += chu_so
        else:
            if chu_so != 0:
                tich *= chu_so
                check = True
    if not check:
        tich = 0
    print(f"{tich} {tong}")