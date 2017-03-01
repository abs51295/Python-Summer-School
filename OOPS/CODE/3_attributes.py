class Car:
    def __init__(self, name):
        self.name = name
        # Default Value
        self.reading = 0

    def change(self):
        self.reading = 10


my_car = Car("BMW")
print(my_car.reading)
my_car.reading = 100
print(my_car.reading)
my_car.change()
print(my_car.reading)
