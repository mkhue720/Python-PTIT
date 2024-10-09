n = int(input())
for i in range(n):
    N = input()
    if N[0] == N[len(N) - 2] and N[1] == N[len(N) - 1]:
        print("YES")
    else:
        print("NO")