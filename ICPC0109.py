# MLE
N = int(input())
for _ in range(N):
    n = int(input())
    A = list(map(int, input().split()))
    first_min = float('inf')
    second_min = float('inf')
    third_min = float('inf')

    for i in A:
        if i < first_min:
            third_min = second_min
            second_min = first_min
            first_min = i
        elif i < second_min:
            third_min = second_min
            second_min = i
        elif i < third_min:
            third_min = i
    result = first_min + second_min + third_min
    print(result)
