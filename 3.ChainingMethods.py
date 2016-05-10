
from flask import Flask
app = Flask(__name__)
class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        return "Price:"+str(self.price)+"\nMax speed:"+str(self.max_speed)+"\nTotal miles:"+str(self.miles)+"\n"
        return self
    def ride(self):
        print "Riding"
        self.miles+=10
        return self
    def reverse(self):
        print "Reversing"
        self.miles-=5
        if self.miles < 0:
            self.miles = 0
        return self

Bike1 = Bike(100,20)
print Bike1.ride().ride().ride().reverse().displayInfo()

Bike2 = Bike(100,20)
print Bike2.ride().ride().reverse().reverse().displayInfo()

Bike3 = Bike(100,20)
print Bike3.reverse().reverse().reverse().displayInfo()

app.run(debug=True)
