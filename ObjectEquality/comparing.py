class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Aman", 25)
p2 = Person("Aman", 25)

print(p1 == p2)   # False different objects in memory, even though data is identical
print(p1 is p2)