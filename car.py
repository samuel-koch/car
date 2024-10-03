class Car:
    def __init__(self ,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    def accelerate(self, increase):
        self.speed += increase
        print(f"Auto ted jede rychlosti {self.speed} km/h")


# vytvoreni objektu

car1 = Car("bmw","i8",2022)
print(car1.brand)
print(car1.model)
car1.accelerate(50)