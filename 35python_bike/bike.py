class Bike(object):
    def __init__ (self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "Price:",self.price,"Max Speed:",self.max_speed,"Miles:", self.miles
    def ride(self):
        self.miles += 10
        print "Riding"
        return self
    def reverse(self):
        if self.miles >= 5: # Prevents miles from going negative.
            self.miles -= 5
        print "Reversing"
        return self

bike1 = Bike("$200", "25mph")
bike2 = Bike("$250", "27mph")
bike3 = Bike("$350", "29mph")

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
