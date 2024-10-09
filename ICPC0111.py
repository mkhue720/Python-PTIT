def rotate_array(A, N, d):
    d = d % N 
    return A[d:] + A[:d]

T = int(input())
for _ in range(T):
    N, d = map(int, input().split())  
    A = list(map(int, input().split())) 
    result = rotate_array(A, N, d)  
    print(" ".join(map(str, result)))
