""" The owner of a store wants a program to track products. Create a product class to fill the following requirements
Attributes: Price, Item Name, Weight, Brand, Status: default "for sale"
Methods: -Sell: changes status to "sold".
-Add Tax: takes tax as decimal as a parameter and returns the price of the item including tax.
-Return: takes reason for return as parameter and changes status accordingly. if item being returned is defective, change status to "defective" and change price to 0. if it is being returned in the box like new mark it "for sale". If the box has been opened, set the status to "used" and apply a 20% discount.
-Display Info: show all product details.
Every method that doesn't have to return something should "return self" so methods can be chained.
"""
# Step 1 complete
class Product(object):
    def __init__(self, price, itemName, weight, brand,):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.status = "for sale" # defaults status to "for sale"
    def displayInfo(self):
        print "Price:", self.price
        print "Item Name:", self.itemName
        print "Weight:",self.weight,"lbs."
        print "Brand:", self.brand
        print "Status:", self.status
        print " " # leaves a gap under the info for better visibility when displaying multiple
        return self
    def sell(self):
        self.status = "sold"
        return self
    def addTax(self, tax):
        self.price += (self.price * tax) # adds the tax into the item price to make the new price include tax
        return self
    def returnItem(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
            return self
        elif reason == "unopened":
            self.status = "for sale"
            return self
        elif reason == "opened":
            self.status = "used"
            self.price = self.price * 0.80
            return self
        else:
            print "ERROR, use reason defective, unopened, or opened" # A reminder for the possible choices of a return when a mistake was entered.

tv = Product(500,'55" LED TV',18,"Samsung") #for testing
tv2 = Product(200, '25" LCD TV',6,"LG")
computer = Product(600,"Epic CPU",7,"Empyre")  ## for testing
# tv.displayInfo().addTax(.08).displayInfo().sell().displayInfo().returnItem("opened").displayInfo() ## for testing
# tv2.displayInfo() # for testing

""" Now build a store to contain our products by making a store class and putting our products into an array.
Attributes: -products: an array of products objects
-location: store address
-owner: store owners name
Methods: -add_product: add a product to the store's product list
-remove_product: remove a product according to the product name
-inventory: print relevant information about each product in the Store
You should be able to test your classes by instantiating new objects of each class and using the outlined methods to demonstrate that they work.
"""
# STEP 2
class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
    def inventory(self):
        for x in self.products:
            x.displayInfo()
        return self
    def add_product(self, name):
        self.products.append(name)
        return self
    def remove_product(self, name):
        self.products.remove(name)
        return self


my_store = Store([tv, tv2, computer], "Pasco", "Matt")
my_store.inventory().remove_product(tv2).inventory().add_product(tv2).inventory() #check inventory, remove 1 item, check inventory, add item to end, check inventory
