N = int(input())
for _ in range(N):
    n = input()
    if n[0] == n[-1]:
        print("YES")
    else:
        print("NO")