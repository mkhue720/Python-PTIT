def robot(n):
    x = 0
    y = 0
    for i in n:
        if i == 'E':
            x += 1
        elif i == 'S':
            y -= 1
        elif i == 'W':
            x -= 1
        elif i == 'N':
            y += 1
        else:
            return "INVALID"
    return f"{x} {y}"

N = int(input())
for _ in range(1, N + 1):
    buoc = input()
    print(robot(buoc))