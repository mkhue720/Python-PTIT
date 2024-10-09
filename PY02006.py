N = int(input())
for _ in range(N):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    check = True
    for i in range(N):
        if A[i] > B[i]:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")