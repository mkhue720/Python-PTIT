class NhanVien:
    dem = 1
    def __init__(self, manv, ten, lythuyet, thuchanh):
        self.manv = 'TS0' + str(manv)
        NhanVien.dem += 1
        self.ten = ten
        self.lythuyet = lythuyet / 10 if lythuyet > 10 else lythuyet
        self.thuchanh = thuchanh / 10 if thuchanh > 10 else thuchanh
    
    def tinh_diem(self):
        return (self.lythuyet + self.thuchanh) / 2
    
    def xep_loai(self):
        diem = self.tinh_diem()
        if diem > 9.5:
            return "XUAT SAC"
        elif diem > 8:
            return "DAT"
        elif diem > 5:
            return "CAN NHAC"
        else:
            return "TRUOT"
        
if __name__ == '__main__':
    N = int(input())
    ds_nv = []
    for i in range(N):
        ten = input()
        lythuyet = float(input())
        thuchanh = float(input())
        nv = NhanVien(i + 1, ten, lythuyet, thuchanh)
        ds_nv.append(nv)
    
    ds_nv.sort(key=lambda x: x.tinh_diem(), reverse=True)
    
    for i in ds_nv:
        print(i.manv, i.ten, '{:.2f}'.format(i.tinh_diem()), i.xep_loai())
