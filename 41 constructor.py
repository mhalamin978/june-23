class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        print("move")
    def draw(self):
        print("drive")

point = Point(10,23)
point.x = 34
print(point.x)
