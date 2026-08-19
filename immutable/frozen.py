from dataclasses import dataclass

@dataclass(frozen=True)   
class Point:
    x: int
    y: int

    def distance_from_origin(self):
        return (self.x**2 + self.y**2) ** 0.5


p = Point(3, 4)
print(p.distance_from_origin())  

# p.x = 5 
p._Point__x = 6
print(p.x)