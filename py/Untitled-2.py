class Car:
 def __init__(self, brand, model, speed):
            self.brand = brand
            self.model = model
            self.speed = speed
 def drive(self):
    print(self.brand, self.model, "is driving at", self.speed, "km/h!")

car1 = Car("toyota", "corolla", 120 )
car2 = Car("bmw", "m2", 140 )
print(car1.brand)
print(car2.brand)

car1.drive()
car2.drive()
