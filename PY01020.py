N = int(input())
for i in range(N):
    n = input().strip()
    if len(n) > 2 and n[-2:] == '86':
        print('YES')
    else:
        print('NO')