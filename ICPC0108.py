#WA
def find(A, N):
    A.sort()
    dem = 0
    for i in range(N-2):
        left = i + 1
        right = N - 1
        while left < right:
            if A[i] + A[left] + A[right] == 0:
                dem += 1
                left += 1
                right -= 1
            elif A[i] + A[left] + A[right] < 0:
                left += 1
            else:
                right -= 1
    return dem

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(find(A, N))