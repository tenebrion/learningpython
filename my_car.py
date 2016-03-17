'''
Created on Feb 29, 2016

@author: michael.f.koegel

Creating a simple car program to focus on classes, interitance, etc.
'''
class Car(object):
    condition =  "new"
    #initializing our values
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
    
    #printing a message about the car
    def display_car(self):
        print ("This is a {} {} with {} MPG".format(self.model, self.color, self.mpg))
    
    def drive_car(self):
        self.condition = "used" #sets car to used if driven

#creating an electric car class that should inherit items from the Car class
class ElectricCar(Car):
    #defining a method that pulls in the proper values
    def __init__(self, model, color, mpg, battery_type):
        Car.__init__(self, model, color, mpg) #have to initialize them from the Car class
        self.battery_type = battery_type #initializing the battery_type value
    #if the car has been driven, change it to like new
    #this will also override the drive_car in the Car class
    def drive_car(self):
        self.condition = "like new"

#initializing the values for an Electric car
my_car = ElectricCar("Tesla", "red", 250, "molten salt")

print(my_car.condition) #prints "New"
my_car.drive_car() #time for a test drive
print(my_car.condition) #should print Like new