class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "Health:",self.health
        return self
a1 = Animal("Ravi",50)
# a1.walk().walk().walk().run().run().display_health() # testing

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog,self).__init__(name, health)
        self.health = 150
    def pet(self):
        self.health += 5
        return self
d1 = Dog("Spot",100)
#d1.walk().walk().walk().run().run().pet().display_health() # testing

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon,self).display_health()
        print "I am a Dragon"
        return self

dr1 = Dragon("Empyre",100)
dr1.fly().display_health().fly().display_health()
a2 = Animal("Test",20)
# a2.display_health() # Checks to make sure it does not contain "I am a Dragon"
# a2.pet() # Checks to make sure pet() will not work.
