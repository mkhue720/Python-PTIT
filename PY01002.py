def check(tinh) :
    tinh = tinh.replace(" ", "")
    a = int(tinh[0])
    b = int(tinh[2])
    c = int(tinh[4])

    if a + b == c :
        print("YES")
    else :
        print("NO")
tinh = input()
check(tinh)
    