import json

def tinh(data, batdau, ketthuc):
    tong = 0
    check = False
    for i in data['flights']:
        nam = int(i['year'])
        if batdau <= nam < ketthuc:
            tong += int(i['passengers'])
            check = True
    if not check:
        return "Invalid"
    return tong

with open('flights.json', 'r') as f:
    data = json.load(f)
N = int(input())
res = []
for _ in range(N):
    batdau, ketthuc = map(int, input().split())
    if batdau > ketthuc:
        res.append("Invalid")
        continue
    else:
        res.append(tinh(data, batdau, ketthuc))
for i in res:
    print(f"{i}")
