class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def show_vehicle_details(self):
        print(f"Vehicle: {self.make} {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, horsepower):
        super().__init__(make, model)
        self.horsepower = horsepower

    def show_car_details(self):
        super().show_vehicle_details()
        print(f"Horsepower: {self.horsepower} HP")

class ElectricCar(Car):
    def __init__(self, make, model, horsepower, battery_capacity):
        super().__init__(make,model,horsepower)
        self.battery_capacity = battery_capacity

    def show_electric_cars(self):
        super().show_car_details()
        print(f"Batterry: {self.battery_capacity} KWh")


#Creating Cars 
print(f"-----------------------------")   

car_010 = Car("Mazda", "CX-5", 250)
car_010.show_car_details()


print(f"-----------------------------")

electric_07 = ElectricCar("Tesla", "Model S", 800, 120)
electric_07.show_electric_cars()

print(f"-----------------------------")
