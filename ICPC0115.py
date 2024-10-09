N = int(input())

gt = [1]

for i in range(1, 10):
    gt.append(gt[-1] * i)

while N > 0:
    n = input()
    sum = 0
    for i in range(0, len(n)):
        sum += gt[int(n[i])]
    if sum == int(n):
        print("Yes")
    else:
        print("No")
    N -= 1