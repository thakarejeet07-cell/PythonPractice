class Dog:
    def speak(self): return "Woof!"

class Cat:
    def speak(self): return "Meow!"

class PetFactory:
    @staticmethod
    def get_pet(pet_type):
        if pet_type == "dog":
            return Dog()
        elif pet_type == "cat":
            return Cat()
        raise ValueError("Unknown pet type")

my_pet = PetFactory.get_pet("dog")
print(my_pet.speak())
    