def check(X):
    if X < 2:
        return False
    for i in range(2, int(X**0.5) + 1):
        if X % i == 0:
            return False
    return True
N, M = map(int, input().split())
A = []
for i in range(N):
    hang = (list(map(int, input().split())))
    for j in range(M):
        if check(hang[j]):
            hang[j] = 1
        else:
            hang[j] = 0
    A.append(hang)
for i in range(N):
    print(*A[i])
