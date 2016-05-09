from flask import Flask
app = Flask(__name__)
class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()
    def display_all(self):
        print "\nPrice:"+str(self.price)+"\nSpeed:"+str(self.speed)+"mph\nFuel:"+str(self.fuel)+"\nMileage:"+str(self.mileage)+"mpg\nTax:"+str(self.tax)+"\n"

Car1 = Car(5000, 120, 'Full', '20')
Car2 = Car(25000, 110, 'Half', '32')

app.run(debug=True)
