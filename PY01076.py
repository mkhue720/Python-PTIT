import math
n = int(input())
for i in range(n):
    a = int(input())
    b = int(input())
    print(math.gcd(a, b))
    # while a != b:
    #     if a > b:
    #         a = a - b
    #     else:
    #         b = b - a
    # print(a)