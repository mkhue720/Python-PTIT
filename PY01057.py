
def check_position(n):
    return n in {2, 3, 5, 7}

def check_digit(n):
    return n in {'2', '3', '5', '7'}

N = int(input())
for _ in range(N):
    n = input()
    check = True
    for i in range(len(n)):
        vt = i
        if check_position(vt):
            if not check_digit(n[i]):
                check = False
                break
        else:
            if check_digit(n[i]):
                check = False
                break
    if check:
        print("YES")
    else:
        print("NO")