class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()

    def start_car(self):
        print("Car Brand:", self.brand)
        self.engine.start()
        print("Car is ready to drive")

car = Car("Honda")
car.start_car()
