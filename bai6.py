def check(n):
    if len(n) % 2 != 0:
        return "NO"
    
    if n[0] == n[2]: 
        return "NO"
    
    for i in range(1, len(n), 2):
        if n[i] != n[1]:
            return "NO"
    return "YES"
N = int(input())
res = []
for _ in range(N):
    n = input()
    res.append(check(n))
for i in res:
    print(i)