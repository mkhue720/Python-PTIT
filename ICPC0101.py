N = int(input())
A = list(map(int, input().split()))
arr = []
for i in A:
    if arr and (arr[-1] + i) % 2 == 0:
        arr.pop()
    else:
        arr.append(i)
print(len(arr))
