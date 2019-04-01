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
  def __init__(self, initial_data):
    self.vehicle_type = initial_data['vehicle_type']
    self.wheel_count = initial_data['wheel_count']
    self.name = initial_data['name']
    self.mpg = initial_data['mpg']
  
  def get_vehicle_type(self):
    return self.vehicle_type

  def get_vehicle_drive(self):
    wheels = self.wheel_count
    if wheels == "no wheels!":
      return "no wheels send it back to the shop"
    else:
      return ("I have %s wheel drive" %(wheels,))


# #2: Create a Motorcycle class that inherits from the Vehicle class and has the
# following properties and methods:
# - all the properties inherited from the Vehicle class
# - method: `pop_wheelie` if `wheel_count` is not equal to 2 then it should return False
#       otherwise return "popped a wheelie!"

def Motorcycle(Vehicle):
  def __init__(self, initial_data):
    super().__init__(initial_data)

  def pop_wheelie(self):
    if self.wheel_count != 2:
      return False
    else:
      return "popped a wheelie!"




# #3: Define a Car class that inherits from the Vehicle class with the following properties and methods:
# - all the properties inherited from the Vehicle class
# - property: `wheel_count` defaults to 4
# - method: `can_drive` that should return 'Vrrooooom Vroooom'


# #4: Define a Truck class that inherits from the Vehicle class with the following properties and methods:
# - all the properties inherited from the Vehicle class
# - method: `rev_engine` that should return a string 'rreevv!'


# Commit when you finish working on these questions!
