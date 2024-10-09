def check_increase(s, end):
    for i in range(1, end + 1):
        if s[i] <= s[i - 1]: 
            return False
    return True

def check_decreasing(s, start):
    for i in range(start + 1, len(s)):
        if s[i] >= s[i - 1]:
            return False
    return True

def check_len(n):
    s = str(n)
    length = len(s)

    if length < 3:
        return False 

    for i in range(1, length - 1):
        if check_increase(s, i) and check_decreasing(s, i):
            return True 

    return False

T = int(input())
for _ in range(T):
    n = int(input())
    if check_len(n):
        print("YES")
    else:
        print("NO")
