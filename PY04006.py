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

    # def check(self):
    #     a = self.p1.distance(self.p2)
    #     b = self.p2.distance(self.p3)
    #     c = self.p1.distance(self.p3)
    #     return a + b > c and a + c > b and b + c > a

    def dien_tich(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        if(max(a, b, c) * 2 >= a + b + c) : print('INVALID')
        else :
            d = sqrt((a + b + c) * (a + b - c) * (b + c - a) * (c + a - b)) / 4
            print('{:.2f}'.format(d))

if __name__ == '__main__':
    t = int(input())
    results = []
    for _ in range(t):
        x1, y1, x2, y2, x3, y3 = map(float, input().split())
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        p3 = Point(x3, y3)
        triangle = Triangle(p1, p2, p3)
        
        # if triangle.check():
        #     results.append(f"{triangle.dien_tich():.2f}")
        # else:
        #     results.append("INVALID")

        results.append(triangle.dien_tich())
    
    for result in results:
        print(result)
