n = int(input())

for i in range(n):
    N = input()
    S = 0
    check = True
    for t in N:
        S += int(t)
    for j in range(2, S):
        if S % j == 0:
            print("NO")
            check = False
            break
    if check:
        print("YES")