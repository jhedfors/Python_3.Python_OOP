class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
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
