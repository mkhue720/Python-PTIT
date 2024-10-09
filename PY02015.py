while True:
    A = list(map(int, input().split()))
    if A == [0, 0, 0, 0]:
        break
    dem = 0
    while len(set(A)) != 1: 
        B = [0] * 4 
        B[0] = abs(A[0] - A[1])
        B[1] = abs(A[1] - A[2])
        B[2] = abs(A[2] - A[3])
        B[3] = abs(A[3] - A[0])
        A = B 
        dem += 1
    print(dem)
