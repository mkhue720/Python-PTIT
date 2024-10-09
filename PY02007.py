# Nhập 10 số nguyên dương từ nhiều dòng
A = []
while len(A) < 10:
    A += list(map(int, input().split()))
dem = set()

for i in A:
    dem.add(i % 42)
print(len(dem))
