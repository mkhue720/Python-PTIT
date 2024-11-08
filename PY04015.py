class KhachHang:
    dem = 1
    def __init__(self, ten, cu, moi):
        self.makh = f"KH{KhachHang.dem:02d}"
        KhachHang.dem += 1
        self.ten = ten
        self.cu = cu
        self.moi = moi

    def tinh_nuoc(self):
        return self.moi - self.cu
    
    def tinh_tien(self):
        nuoc = self.tinh_nuoc()
        if nuoc > 100:
            return int(round((50 * 100 + 50 * 150 + (nuoc - 100) * 200) * 1.05, 0))
        elif nuoc > 50:
            return int(round((50 * 100 + (nuoc - 50) * 150) * 1.03, 0))
        else:
            return int(round(nuoc * 100 * 1.02, 0))
        
if __name__ == '__main__':
    N = int(input())
    ds_kh = []
    for _ in range(N):
        ten = input()
        cu = int(input())
        moi = int(input())
        kh = KhachHang(ten, cu, moi)
        ds_kh.append(kh)
    
    ds_kh.sort(key=lambda x: x.tinh_tien(), reverse=True)
    
    for i in ds_kh:
        print(f"{i.makh} {i.ten} {i.tinh_tien()}")