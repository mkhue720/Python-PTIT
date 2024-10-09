#MLE
MAX = 2 * 10**6
arr = [0] * (MAX + 1)
def check():
    for i in range(2, MAX + 1):
        if arr[i] == 0:
            for j in range(i, MAX + 1, i):
                arr[j] += i
check()

N = int(input())
n = [int(input()) for _ in range(N)]
res = 0
for i in n:
    res += arr[i]
print(res)
