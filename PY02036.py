# wa
import math
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N = int(input())
A = list(map(int, input().split()))
kq = []
for i in range(N):
    for j in range(i + 1, N):
        if gcd(A[i], A[j]) == 1:
            kq.append((min(A[i], A[j]), max(A[i], A[j])))
kq.sort()
for i in kq:
    print(i[0], i[1])