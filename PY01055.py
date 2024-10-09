n = int(input())
for i in range(n):
    a = input()
    so_luong_chu_so = len(a)
    if so_luong_chu_so % 2 == 0:
        print("NO")
        continue
    if a[0] == a[1]:
        print("NO")
        continue
    check = True
    for i in range(0, so_luong_chu_so, 2):
        if a[i] != a[0]:
            print("NO")
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")