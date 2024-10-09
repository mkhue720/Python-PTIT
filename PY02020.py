N = int(input())
A = list(map(float, input().split()))
min = A[0]
max = A[0]

for i in A:
    if i < min:
        min = i
    if i > max:
        max = i
tong = 0
dem = 0

for i in A:
    if i != min and i != max:
        tong += i
        dem += 1
if dem > 0:
    tb = tong / dem
else:
    tb = 0
print(f"{tb:.2f}")
