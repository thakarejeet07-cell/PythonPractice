from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age: int

p1 = Person("Aman", 25)
p2 = Person("Aman", 25)

print(p1 == p2)  
print(p1 in {p1, p2})  

people_dict = {p1: "Engineer"}
print(people_dict[p2])