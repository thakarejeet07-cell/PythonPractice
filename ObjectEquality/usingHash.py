class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash((self.name, self.age))    

p1 = Person("Aman", 25)
p2 = Person("Aman", 25)


people_dict = {p1: "Software Engineer"}
print(people_dict[p2])


unique_people = {Person("Aman", 25), Person("Aman", 25), Person("Riya", 22)}
print(len(unique_people))