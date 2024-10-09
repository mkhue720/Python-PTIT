n = int(input())
for i in range(n):
    a = input()
    check = True
    for t in a:
        if t != '4' and t != '7':
            print("NO")
            check = False
            break
    if check:
        print("YES")