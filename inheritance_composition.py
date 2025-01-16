class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def show_vehicle_info(self):
        print(f"Vehicle: {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, horsepower):
        super().__init__(make, model)
        self.horsepower = horsepower
    def show_car_info(self):
        super().show_vehicle_info()
        print(f"Horsepower: {self.horsepower} HP")

class Truck(Vehicle):
    def __init__(self, make, model, payload_capacity):
        super().__init__(make, model)
        self.payload_capacity = payload_capacity

    def show_truck_info(self):
        super().show_vehicle_info()
        print(f"Payload Capacity: {self.payload_capacity} tons")

#Composition begins here
        
class Garage:
    def __init__(self):
        self.vehicle = []

    def add_vehicle(self,vehicle):
        self.vehicle.append(vehicle)
    
    def show_vehicles(self):
        for vehicle in self.vehicle:
            vehicle.show_vehicle_info()
            print("-------------------------------")


#Creating Instances of Cars and Trucks
car_1 = Car("Honda", "Fit", 230)
car_2 = Car("Toyota", "V8", 500)

truck_1 = Truck("Ford", "Ranger", 2)
truck_2 = Truck("Tata", "FH-120", 8)

#Creating a garage inventory

garage = Garage()
garage.add_vehicle(car_1)
garage.add_vehicle(car_2)
garage.add_vehicle(truck_1)
garage.add_vehicle(truck_2)

#Show what we have in our garage

garage.show_vehicles()




