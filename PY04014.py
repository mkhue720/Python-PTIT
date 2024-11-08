class HocSinh:
    dem = 1

    def __init__(self, ten, toan, tv, nn, vl, hh, sh, ls, dl, gdcd, cn):
        self.mahs = f"HS{HocSinh.dem:02d}"
        HocSinh.dem += 1
        self.ten = ten
        self.toan = toan
        self.tv = tv
        self.nn = nn
        self.vl = vl
        self.hh = hh
        self.sh = sh
        self.ls = ls
        self.dl = dl
        self.gdcd = gdcd
        self.cn = cn

    def tb_diem(self):
        tong_diem = (self.toan * 2 + self.tv * 2 + self.nn + self.vl + self.hh + self.sh + self.ls + self.dl + self.gdcd + self.cn)
        diemtb = tong_diem / 12
        return round(diemtb + 0.01, 1)
    
    def check(self):
        if self.tb_diem() >= 9:
            return "XUAT SAC"
        elif self.tb_diem() >= 8:
            return "GIOI"
        elif self.tb_diem() >= 7:
            return "KHA"
        elif self.tb_diem() >= 5:
            return "TB"
        else:
            return "YEU"
    
if __name__ == '__main__':
    N = int(input())
    ds_hs = []
    for _ in range(N):
        ten = input()
        toan, tv, nn, vl, hh, sh, ls, dl, gdcd, cn = map(float, input().split())
        hs = HocSinh(ten, toan, tv, nn, vl, hh, sh, ls, dl, gdcd, cn)
        ds_hs.append(hs)
    sorted_hs = sorted(ds_hs, key=lambda x: x.tb_diem(), reverse=True)
    for i in sorted_hs:
        print(f"{i.mahs} {i.ten} {i.tb_diem()} {i.check()}")