# This is the main thing. The Biggest container to which we are adding everything else.
# It has no dimension or any parameter
# The farm class has a variable farm_inventory to which is assiged an empty list[] to receive every detail about tools, animal, or anything that is in the farm
# The farm also has three functions: for adding tools to the farm, for adding animal to the farm, and for displaying the inventory

class Farm:
    def __init__(self) -> None:
        self.farm_inventory = []

    def add_tool_to_farm(self, tool):
        self.farm_inventory.append(tool) 

    def add_animal_to_farm(self, animal):
        self.farm_inventory.append(animal)

    def dispaly_farm_inventory(self):

        for item in self.farm_inventory:
            if isinstance(item, Machinery):
                print(item.show_machinery_details())
            elif isinstance(item, HandDriven):
                print(item.show_hand_driven())
            elif isinstance(item, FarmTool): 
                print(item.show_farmtool_details())
            elif isinstance (item, Cattle):
                print(item.show_cattle_details())
            elif isinstance(item, Chicken):
                print(item.show_chicken_details())
            elif isinstance(item, Poultry):
                print(item.show_poultry_info())
            elif isinstance(item, Animal):
                print(item.show_animal_details())
            else:
                print("Unavailable in the Inventory")
            print("break--------------------------------------------------------------------end of break")

      
class FarmTool:
    def __init__(self, serial, category, hand_driven = None) -> None:
        self.serial = serial
        self.category = category
        self.hand_driven = hand_driven

    def show_farmtool_details(self):
        details = f"Serial Number: {self.serial}, Category: {self.category}"
        if self.hand_driven:
            details += f", Number Of Wheels: {self.hand_driven.number_of_wheels}, Material: {self.hand_driven.material}"
        return details

class HandDriven():
    def __init__(self, number_of_wheels, material) -> None:
        self.number_of_wheels = number_of_wheels
        self.material = material
    def show_hand_driven(self):
        return f"Number of Wheels: {self.number_of_wheels}, Material: {self.material}"
    
#### We should add a class AnimalDriven which is by composition extended from the FarmTool (Not by Inheritance) 

class Machinery(FarmTool):
    def __init__(self, serial, category, fuel_consumption) -> None:
        super().__init__(serial, category)
        self.fuel_consumption = fuel_consumption

    def show_machinery_details(self):
        return f"{super().show_farmtool_details()}, Fuel Consumption: {self.fuel_consumption} litres/mile"

class Animal:
    def __init__(self, age, color) -> None:
        self.age = age 
        self.color = color

    def show_animal_details(self):
        return f"Age: {self.age} years, Color: {self.color}"


class Cattle(Animal):
    def __init__(self, age, color, name) -> None:
        super().__init__(age, color)
        self.name = name

    def show_cattle_details(self):
        return f"{super().show_animal_details()}, Name: {self.name}"

class Poultry(Animal):
    def __init__(self, age, color,type) -> None:
        super().__init__(age, color)
        self.type = type

    def show_poultry_info(self):
        return f"{super().show_animal_details()}, Type: {self.type}"
    
class Chicken(Poultry):
    def __init__(self, age, color, type, gender) -> None:
        super().__init__(age, color, type)
        self.gender = gender

    def show_chicken_details(self):
        return f"{super().show_poultry_info()}, Gender: {self.gender}"
    

# Also add a subclass Chicken which Inherits from Poultry and make some of its attributes private
    
# Let's Add some Real Data/Create Objects


farmtool_1 = FarmTool("1234HM", "Irrigation")
farmtool_2 = FarmTool("4567CD", "Land Preparation")
farmtool_3 = Machinery("001123GH", "Land Preparation", 16)
hand_driven_tool = HandDriven(4, "Steel")
farmtool_4 = FarmTool("7890HD", "Hand Tool", hand_driven=hand_driven_tool)

animal_1 = Animal(12, "brown")
animal_2 = Cattle(3, "black", "Clifford")
animal_3 = Poultry(0.5, "white", "Layer")
animal_4 = Chicken(1, "Brown", "Broiler", "Female")

animal_extra = (6, "babbooon")

farm_inventory = Farm()

#Add Tools to Farm
farm_inventory.add_tool_to_farm(farmtool_1)
farm_inventory.add_tool_to_farm(farmtool_2)
farm_inventory.add_tool_to_farm(farmtool_3)
farm_inventory.add_tool_to_farm(farmtool_4)

#Add Animals to Farm
farm_inventory.add_animal_to_farm(animal_1)
farm_inventory.add_animal_to_farm(animal_2)
farm_inventory.add_animal_to_farm(animal_3)
farm_inventory.add_animal_to_farm(animal_4)

farm_inventory.dispaly_farm_inventory()


