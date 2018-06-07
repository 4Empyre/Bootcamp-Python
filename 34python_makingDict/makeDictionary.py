# Take 2 lists, and combine them into 1 Dictionary
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "Bartholemule"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    temp = zip(list1,list2)
    new_dict = dict(temp)
    return new_dict
print make_dict(name, favorite_animal)
