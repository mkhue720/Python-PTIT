import re

def tim_max(s):
    numbers = re.findall(r'\d+', s)
    if numbers:
        return max(map(int, numbers))
    else:
        return None
T = int(input())
for _ in range(T):
    s = input()
    result = tim_max(s)
    if result is not None:
        print(result)
