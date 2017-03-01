class Car:
    def __init__(self, name):
        self.name = name
        # Default Value
        self.reading = 0

    def change(self):
        self.reading = 10

    def base(self):
        print("In the base class")


class Mycar(Car):
    def __init__(self, name):
        super().__init__(name)

    def change(self):
        self.reading = 50

    def derived(self):
        print("In the derived class")


my_car = Car("BMW")
# Polymorphism achieved here
print(my_car.reading)

car_2 = Mycar("Tesla")
# Here , too
print(car_2.reading)
car_2.change()
print(car_2.reading)

car_2.derived()
car_2.base()
my_car.base()
