n = int(input())
for _ in range(n):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = []
    b = []
    check = True
    A.sort()
    B.sort()

    for i in range(N):
        if A[i] > B[i]:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")