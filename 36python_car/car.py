class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price >= 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()
    def display_all(self):
        print "Price: "+str(self.price)
        print "Speed: "+self.speed
        print "Fuel: "+self.fuel
        print "Mileage: "+self.mileage
        print "Tax: "+str(self.tax)
        print " "

car1 = Car(18000,"160mph","full","20mpg")
car2 = Car(12000,"155mph","half full","24mpg")
car3 = Car(8000,"150mph","half full","26mpg")
car4 = Car(5000,"140mph","almost empty","30+mpg")
car5 = Car(80000,"180mph","full","17mpg")
car6 = Car(160000,"200mph","full","12mpg")
