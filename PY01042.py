N = int(input())
for _ in range(N):
    n = input().strip()
    check = True
    for i in n:
        if i not in {'0', '1', '2'}:
            check = False
            break

    if check:
        print('YES')
    else:
        print('NO')
