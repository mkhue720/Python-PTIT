def check(arr):
    f = {}
    for i in arr:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    f_max = max(f.values())
    element = max(f, key=f.get)
    return element, f_max

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    element, frequency = check(A)
    if frequency > N / 2:
        print(element)
    else:
        print("NO")