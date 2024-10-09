def lam_tron(n):
    bac = 10
    while n >= bac:
        if n % bac >= bac / 2:
            n = (n // bac + 1) * bac
        else:
            n = (n // bac) * bac
        bac *= 10 
    return n

so_bo_test = int(input())

for _ in range(so_bo_test):
    n = int(input())
    print(lam_tron(n))
