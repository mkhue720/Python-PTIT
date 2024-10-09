def check_reversible(n):
    m = 0
    tmp = n
    while n != 0:
        m = m * 10 + n % 10
        n //= 10
    return tmp == m

def check_digit(N):
    for i in N:
        if i not in {'0', '2', '4', '6', '8'}:
            return False 
    return True  

T = int(input())
for _ in range(T):
    N = input()
    arr = []
    for i in range(22, int(N), 22):
        if check_reversible(i) and check_digit(str(i)) and len(str(i)) % 2 == 0:
            arr.append(str(i))
    print(" ".join(arr))