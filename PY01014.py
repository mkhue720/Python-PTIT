a, K, N = map(int, input().split())

bd = (K - a % K) if a % K != 0 else K

found = False

for i in range (bd, N - a + 1, K) :
    print(i, end = " ")
    found = True
if not found :
        print(-1)