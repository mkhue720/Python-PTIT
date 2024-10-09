#IR
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def is_valid(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

    def chu_vi(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        return round(a + b + c, 3)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x1, y1, x2, y2, x3, y3 = map(float, input().split())
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        p3 = Point(x3, y3)       
        triangle = Triangle(p1, p2, p3)       
        if triangle.is_valid():
            print(f"{triangle.chu_vi():.3f}")
        else:
            print("INVALID")
