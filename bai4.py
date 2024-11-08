N = int(input())
doi = []
for _ in range(N):
    ten = input()
    diem, hieuso, fairplay = map(int, input().split())
    doi.append((ten, diem, hieuso, fairplay))
sapxep = sorted(doi, key=lambda x: (-x[1], -x[2], -x[3]))
for i in sapxep:
    print(f"{i[0]} {i[1]} {i[2]} {i[3]}")
