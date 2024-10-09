def check_snt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def check_chu_so(n):
    S = 0
    for i in range(len(n)):
        chu_so = int(n[i])
        S += int(n[i])
        if i % 2 == 0:
            if chu_so % 2 != 0:
                return 'NO'
        else:
            if chu_so % 2 == 0:
                return 'NO'
    if not check_snt(S):
        return 'NO'
    return 'YES'
n = int(input())
for i in range(n):
    a = input()
    print(check_chu_so(a))

