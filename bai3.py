def minkowski (x, y, p):
    if len(x) != len(y):
        return "INVALID"
    kc = sum(abs(x[i] - y[i]) ** p for i in range(len(x))) ** (1/p)
    return f"{kc:.5f}"

N = int(input())
res = []
for _ in range(N):
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))
    p = int(input())
    res.append(minkowski(x, y, p))
for i in res:
    print(i)