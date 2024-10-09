N = int(input())
A = list(map(int, input().split()))
arr = [False] * (N + 1)
for i in A:
    if i <= N:
        arr[i] = True
for i in range(1, N + 1):
    if not arr[i]:
        print(i)
        break
else:
    print(N + 1)
