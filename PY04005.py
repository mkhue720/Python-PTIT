#IR
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def check(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        return a + b > c and a + c > b and b + c > a

    def chu_vi(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        return "{:.3f}".format(a + b + c)

if __name__ == '__main__':
    t = int(input())
    res = []
    for _ in range(t):
        x1, y1, x2, y2, x3, y3 = map(float, input().split())
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        p3 = Point(x3, y3)       
        triangle = Triangle(p1, p2, p3)       
        if triangle.check():
            res.append(triangle.chu_vi())
        else:
            res.append("INVALID")
    for result in res:
        print(result)