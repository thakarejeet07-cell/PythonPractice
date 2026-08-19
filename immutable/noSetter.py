class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


    def __str__(self):
        return f"Point({self.__x}, {self.__y})"


p = Point(3, 4)
print(p.x, p.y)  

p.x = 5 
