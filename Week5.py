#class Car:
   # color = "red"
   # model = "Toyota"

    #Method/behavior to display car details
   # def drive(self):
       # print("The car is driving")
   # def stop(self):
        #print("The car has stopped")
   # def honk(self):
        #print("The car is honking")    

#my_car = Car() # Creating an instance of the Car class
#my_car.drive() # Calling the drive method
#my_car.stop() # Calling the stop method
#my_car.honk() # Calling the honk method
# print(my_car.color)  # Accessing the color attribute     




class Person:
    # Constructor to initialize instance variables
    def __init__(self, name, age):
        self.name = name # Instance variable for name
        self.age = age # Instance variable for age

personDetails = Person("John", 30) # Creating an instance of the Person class
print(personDetails.name) # Accessing the name attribute
print(personDetails.age) # Accessing the age attribute