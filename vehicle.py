class Vehicle():
    def __init__ (self, max_speed, milage):
       
     self.max_speed = max_speed
     self.milage = milage
model = Vehicle(220, 18)
print("Model max speed:",model.max_speed)
print("Model milage:",model.milage)