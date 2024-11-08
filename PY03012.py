class SinhVien:
    def __init__(self, ten, bai_dung, so_submit):
        self.ten = ten
        self.bai_dung = bai_dung
        self.so_submit = so_submit

def sap_xep_danh_sach(ds_sv):
    return sorted(ds_sv, key=lambda sv: (-sv.bai_dung, sv.so_submit, sv.ten))

N = int(input())
danh_sach_sv = []
for _ in range(N):
    ten = input().strip()
    bai_dung, so_submit = map(int, input().split())
    danh_sach_sv.append(SinhVien(ten, bai_dung, so_submit))

danh_sach_sv_sap_xep = sap_xep_danh_sach(danh_sach_sv)

for sv in danh_sach_sv_sap_xep:
    print(sv.ten, sv.bai_dung, sv.so_submit)
