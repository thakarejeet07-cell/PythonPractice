class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.name == other.name and self.grade == other.grade

    def __it__(self,other):
        return self.grade < other.grade


    def __str__(self):
        return f"{self.name} (Grade: {self.grade})"


students = [
    Student("Alice", 85),
    Student("Bob", 92),
    Student("Charlie", 78),
]

students.sort()
for s in students:
    print(s)    