class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self,other):
        if not isinstance(other,Person):
            return False
        return self.name == other.name and self.age == other.age


p1 = Person("Aman", 25)
p2 = Person("Aman", 25)
p3 = Person("Riya", 22)

print(p1 == p2)  
print(p1 == p3)   
print(p1 == "not a person")          