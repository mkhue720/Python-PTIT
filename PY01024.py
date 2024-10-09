def check(N) :
    N_str = str(N)
    S = sum(int(i) for i in N_str)

    if S % 10 != 0 :
        return "NO"
    
    for i in range(len(N_str) - 1) :
        if abs(int(N_str[i]) - int(N_str[i + 1])) != 2 :
            return "NO"
        
    return "YES"

n = int(input())

for i in range(n) :
    N = input()
    print(check(N))