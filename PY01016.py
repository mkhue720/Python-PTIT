def decode(s):
    decoded = ""
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        count = int(s[i])
        i += 1
        decoded += char * count
    return decoded
t = int(input())
for _ in range(t):
    s = input()
    print(decode(s))
