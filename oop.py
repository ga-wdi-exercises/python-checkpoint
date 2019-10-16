# 1: Define a Vehicle class with the following properties and methods:
# - `vehicle_type`
# - `wheel_count`
# - `name`
# - `mpg`, a 'dict', with the following properties:
#     - `city`
#     - `highway`
#     - `combined`
# - `get_vehicle_type` should return the `vehicle_type`
# - `get_vehicle_drive` if the `wheel_count` for that class is "no wheels!" then
#     it should return "no wheels send it back to the shop"
#     otherwise it should return "I have {self.wheel_count} wheel drive" as a formatted string
#
# Your Vehicle class should take one extra argument in the __init__ method (a `dict`) with the above
# attributes. Define the properties on the class from the dict that is passed in.
# 
# Here's an example of the dict that will be passed in to your class:
#
# vehicle_dict_vehicle = {
#     "vehicle_type": "Vehicle",
#     "wheel_count": 'no wheels!',
#     "mpg": {
#         "city": 19,
#         "highway": 30,
#         "combined": 27
#     },
#     "name": "Unidentified Flying Object",
# }
class Vehicle:
    def __init__(self,vehicle_type,wheel_count,mpg,name):
        self.vehicle_type = vehicle_type
        self.wheel_count = wheel_count
        self.mpg = mpg
        self.name = name
    
    def get_vehicle_type(self):
        print(self.vehicle_type)
    
    def get_vehicle_drive(self):
        if self.wheel_count == "no wheels!":
            print("no wheels send it back to the shop")
        else:
            print(" I have {} wheel drive".format(self.wheel_count))

tester = Vehicle("Vehicle",3,27,"Unidentified Flying Object")
tester.get_vehicle_type()
tester.get_vehicle_drive()
 
 #Not sure how you put an object in the init for an instance of a class. couldn't get it to work but this works


# #2: Create a Motorcycle class that inherits from the Vehicle class and has the
# following properties and methods:
# - all the properties inherited from the Vehicle class
# - method: `pop_wheelie` if `wheel_count` is not equal to 2 then it should return False
#       otherwise return "popped a wheelie!"

class Motorcycle(Vehicle):
    pass

    def pop_wheelie(self):
        if self.wheel_count == 2:
            print("popped a wheelie!")
        else:
            print(False)
me= Motorcycle("Motorcycle", 2,2,"hi")
me.pop_wheelie()
# #3: Define a Car class that inherits from the Vehicle class with the following properties and methods:
# - all the properties inherited from the Vehicle class
# - property: `wheel_count` defaults to 4
# - method: `can_drive` that should return 'Vrrooooom Vroooom'

class Car(Vehicle):
    def __init__(self,mpg,name):
        self.vehicle_type = "Car"
        self.wheel_count = 4
        self.mpg = mpg
        self.name = name

    def can_drive(self):
        print("Vrrooooom Vroooom")
me = Car(5,"Will")
me.can_drive()
# #4: Define a Truck class that inherits from the Vehicle class with the following properties and methods:
# - all the properties inherited from the Vehicle class
# - method: `rev_engine` that should return a string 'rreevv!'
class Truck(Vehicle):
    def __init__(self,mpg,name):
        self.vehicle_type = "Car"
        self.wheel_count = 4
        self.mpg = mpg
        self.name = name

    def rev_engine(self):
        print("rreevv!")

me = Truck("Truck", 4, 5, "william")
me.rev_engine()


# Commit when you finish working on these questions!
