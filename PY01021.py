def check(s):
    char = []
    S = 0
    for i in s:
        if i.isdigit():
            S += int(i)
        else:
            char.append(i)
    char.sort()
    res = ''.join(char) + str(S)
    return res

N = int(input())
for _ in range(N):
    s = input().strip()
    print(check(s))