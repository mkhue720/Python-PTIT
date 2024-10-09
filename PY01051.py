def check_reversible(n):
    m = 0
    tmp = n
    while n != 0:
        m = m * 10 + n % 10
        n //= 10
    if tmp == m:
        return True
    return False

T = int(input())
for _ in range(T):
    N = input()
    S = 0
    for i in N:
        S += int(i)
    if S > 9 and check_reversible(S):
        print("YES")
    else:
        print("NO")