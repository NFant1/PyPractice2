#Demonstrating multiple functions within a python class being called

#Class 'Car' that contains year and model functions
class Car:
    #Initialization function to set variables within scope of 'Car' class
    def __init__(self, CarYear, CarModel):
        self.CarYear = CarYear
        self.CarModel = CarModel

    #'Year' function that determines whether car is old or new
    def Year(self, CarYear):

        self.CarYear = CarYear

        if(int(CarYear) <= 2017):

            print("Car: Old")

        elif(int(CarYear) > 2017):

            print("Car: New")

    #'Model' function to determine what kind of person you are 
    #based on the vehicle you drive
    def Model(self, CarModel):

        self.CarModel = CarModel

        if(CarModel == 'Nissan'):

            print("You're a fast driver!")

        elif(CarModel == 'Toyota'):

            print("You like reliable Cars!")
            
        elif(CarModel == 'Mercedes'):

            print("You like the appearance of being rich!") 

#Takes user input and stores it in 'yearInput' variable
yearInput = input("Year of vehicle: ")
#Takes user input and stores it in 'modelInput' variable
modelInput = input("Type of Model: ")

#Sets 'Car' class as 'carData' object
carData = Car(yearInput, modelInput)

#Calls the 'Year' function inside the 'Car' class
carData.Year(yearInput)
#Calls the 'Model' function inside the 'Car' class
carData.Model(modelInput)
