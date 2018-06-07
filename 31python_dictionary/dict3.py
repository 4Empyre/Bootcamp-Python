cars = {
"first": "88 Acura Integra LS",
"second": "94 Acura Integra GSR",
"third": "85 Nissan 300ZX turbo",
"fourth": "04 Subaru STI",
"fifth": "92 Mazda Miata turbo",
"sixth": "89 Nissan 240SX SR20"
}

def listCars(cars):
    for key,data in cars.iteritems():
        print "My",key,"car was a",data
listCars(cars)
