class Rectangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def area(self):
        return self.width * self.height
    
    def formatted_color(self):
        c = str(self.color)
        return c[0].upper() + c[1:].lower()
    

if __name__ == '__main__':
    arr = input().split() 
    if int(arr[0]) > 0 and int(arr[1]) > 0: 
        r = Rectangle(int(arr[0]), int(arr[1]), arr[2]) 
        print('{} {} {}'.format(r.perimeter(), r.area(), r.formatted_color())) 
    else: 
        print("INVALID")