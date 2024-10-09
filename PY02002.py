N = int(input())
f = [0] * 100
f[1] = 1
f[2] = 1

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(3, b + 1):
        f[i] = f[i - 1] + f[i - 2]
    for i in range(a, b + 1):
        print(f[i], end=" ")
    print()