N = int(input())
check = True
for _ in range(N):
    n = int(input())
    A = str(n)
    for i in range(len(A) - 2):
        if i != i + 2:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")
