def encode(K, S):
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    encoded = ""
    for char in S:
        index = P.index(char)
        new = (index + K) % 28
        encoded += P[new]
    return encoded[::-1]
while True:
    data = input()
    K, S = data.split()
    K = int(K)
    if K == 0:
        break
    result = encode(K, S)
    print(result)
