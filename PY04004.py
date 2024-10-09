class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rutGon(self):
        a = self.tu
        b = self.mau
        while b != 0:
            a, b = b, a % b
        self.tu //= a
        self.mau //= a

    def tong(self, other):
        tu = self.tu * other.mau + self.mau * other.tu
        mau = self.mau * other.mau
        return PhanSo(tu, mau)

    def __str__(self):
        return f"{self.tu}/{self.mau}"

if __name__ == '__main__':
    tu1, mau1, tu2, mau2 = map(int, input().split())
    ps1 = PhanSo(tu1, mau1)
    ps2 = PhanSo(tu2, mau2)
    ps1.rutGon()
    ps2.rutGon()
    ps = ps1.tong(ps2)
    ps.rutGon()
    print(ps)
