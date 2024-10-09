def encode(s):
    encoded = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        encoded += str(count) + s[i]
        i += 1
    return encoded
t = int(input())
for _ in range(t):
    s = input()
    print(encode(s))
