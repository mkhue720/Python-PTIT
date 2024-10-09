N = int(input())
A = list(map(int, input().split()))
dem = 0

for i in range(N):
    for j in range(i + 1, N):
        if A[i] > A[j]:
            dem += 1
print(dem)