# Introducing composition with various classes (Engine, Wheels) as part of Car.


class Car:
    def __init__(self, make, model, engine, wheels):
        self.make = make
        self.model = model
        self.engine = engine
        self.wheels = wheels 
    
    def display_car_info(self):
        print(f"Car: {self.make} {self.model}, Engine: {self.engine.horsepower} HP, {self.engine.type}, Wheels: {self.wheels.size} inches, {self.wheels.type}" )


class Engine:
    def __init__(self, horsepower, type):
        self.horsepower = horsepower
        self.type = type 

    def show_engine_properties(self):
        return f"Horsepower: {self.horsepower} HP, Type: {self.type}"


class Wheels:
    def __init__(self, size, type):
        self.size = size
        self.type = type

    def show_wheel_specs(self):
        return f"Size: {self.size}, Type: {self.type}"

#Creating Car Objects 

#Toyota 
toyota_engine = Engine(150, "Petrol")
toyota_wheels = Wheels(17, "Alloy")
car_001 = Car("Toyota", "Corolla", toyota_engine, toyota_wheels)

#Audi
audi_engine = Engine(180, "Diesel")
audi_wheels = Wheels(18, "Platinum")
car_002 = Car ("Audi", "Q6 e-tron", audi_engine, audi_wheels)

car_001.display_car_info()
car_002.display_car_info()







