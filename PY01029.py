from math import gcd
def ham_dao(s):
    str = ""
    for i in s:
        str = i + str
    return str

t = int(input())
for _ in range(t):
    s = input()
    if (gcd(int(s), int(ham_dao(s))) == 1):
        print("YES")
    else:
        print("NO")
