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

    def __str__(self):
        return f"{self.tu}/{self.mau}"

if __name__ == '__main__':
    tu, mau = map(int, input().split())
    ps = PhanSo(tu, mau)
    ps.rutGon()
    print(ps)
