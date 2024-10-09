n = int(input())
N = str(n)
dem = 0
for i in N:
    if i == '4' or i == '7':
        dem += 1
if dem == 4 or dem == 7:
    print("YES")
else:
    print("NO")     