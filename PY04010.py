class Thisinh:
    def __init__(self, ten, ns, d1, d2, d3):
        self.ten = ten
        self.ns = ns
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3

    def tong_diem(self):
        return self.d1 + self.d2 + self.d3
    
    def __str__(self):
        return f"{self.ten} {self.ns} {self.tong_diem()}"
    
if __name__ == '__main__':
    ten = input()
    ns = input()
    d1 = input()
    d2 = input()
    d3 = input()
    thisinh = Thisinh(ten, ns, float(d1), float(d2), float(d3))
    print(thisinh)
