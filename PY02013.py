while True:
    N = int(input())
    if N == 0:
        break
    dem = 1 
    while N != 1:
        if N % 2 == 0:
            N = N // 2
        else:
            N = N * 3 + 1
        dem += 1
    print(dem)
