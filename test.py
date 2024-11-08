import json

with open('flights.json', 'r') as file:
    data = json.load(file)
data = data['flights']
for i in range(int(input())):
    a, b = [int(i) for i in input().split()]
    kq = 0
    for fl in data:
        if int(fl['year']) >= a and int(fl['year']) < b:
            kq += int(fl['passengers'])
    if kq == 0:
        print("Invalid")
    else:
        print(kq)