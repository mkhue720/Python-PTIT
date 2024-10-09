import re

def tim_min(s):
    numbers = re.findall(r'\d+', s)
    if numbers:
        return min(map(int, numbers))
    else:
        return None
T = int(input())
for _ in range(T):
    s = input()
    result = tim_min(s)
    if result is not None:
        print(result)
