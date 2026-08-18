class Engine:
    def start(self):
        print("Engine starting...")

    def stop(self):
        print("Engine stopping...")

class electricEngine:
    def start(self):
        print(" electric Engine starting...")

    def stop(self):
        print("electric Engine stopping...")            


class Car:
    def __init__(self, make):
        self.make = make
        self.engine = Engine()

    def start(self):
        print(f"{self.make} is starting")
        self.engine.start()      

    def stop(self):
        self.engine.stop()
        print(f"{self.make} has stopped")


car = Car("Toyota")
car.engine =  electricEngine()
car.start()
car.stop()