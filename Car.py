class Car:
    #Properties
    color = ""
    brand = ""
    number_of_wleels = 4
    number_of_seate = 4
    maxspeed = 0

    #Constructor
    def __init__(self, color, brand, number_of_wleels, number_of_seate, maxspeed):
        self.color = color
        self.brand = brand
        self.number_of_seate = number_of_seate
        self.number_of_wleels = number_of_wleels
        self.maxspeed = maxspeed

    #Create metthod set coler
    def setcoler(self, x):
        self.color = x


    def setbrand(self, x):
        self.brand = x


    def setspeed(self, x):
        self.maxspeed = x


    def printdata(self):
        print("Color of this car is", self.color)
        print("Brand of this car is", self.brand)
        print("Max speed of this car is", self.maxspeed)


    
    #deconstructor
    def __del__(self):
        print()


        
     