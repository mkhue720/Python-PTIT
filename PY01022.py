def sum(n):
    return sum(int(i) for i in str(n))

def count(n):
    dem = 0
    while abs(n) >= 10:
        n = sum(n)
        dem += 1
    return dem
n = input().strip() 
n = int(n) 
res = count(n)
print(res)
