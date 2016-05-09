# Create a new class called  Bike with the following properties/attributes:
#
# price
# max_speed
# miles
# Create 3 instances of the Bike class.
#
# Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.
#
# Add the following functions to this class:
#
# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().
#
# What would you do to prevent the instance from having negative miles?

from flask import Flask
app = Flask(__name__)
class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    # def __new__ (self, price, max_speed, miles):
    #     self.price = 500
    #     self.max_speed = 5
    #     self.miles = 0
    def displayInfo(self):
        return "Price:"+str(self.price)+" Max speed:"+str(self.max_speed)+"Total miles:"+str(self.miles)
    def ride(self):
        print "Riding"
        self.miles+=10
    def reverse(self):
        print "Reversing"
        self.miles-=5
        if self.miles < 0:
            self.miles = 0

Bike1 = Bike(100,20)
Bike1.ride()
Bike1.ride()
Bike1.ride()
Bike1.reverse()
print Bike1.displayInfo()

Bike2 = Bike(100,20)
Bike2.ride()
Bike2.ride()
Bike2.reverse()
Bike2.reverse()
print Bike2.displayInfo()

Bike3 = Bike(100,20)
Bike3.reverse()
Bike3.reverse()
Bike3.reverse()
print Bike3.displayInfo()
app.run(debug=True)
