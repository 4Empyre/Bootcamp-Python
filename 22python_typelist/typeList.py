def typeList(x):
    total = 0.0
    newString = ""
    for i in x:
        if isinstance(i, int):
            total += i
        elif isinstance(i, float):
            total += i
        elif isinstance(i, str):
            newString = newString + i + " "

    if (total != 0.0) & (newString != ""):
        print ("The list you entered has a mix of numbers and strings.")
        print ("Total: " + str(total))
        print ("New string: " + newString)
    elif (total != 0.0) & (newString == ""):
        print ("The list you entered has only numbers.")
        print ("Total: " + str(total))
    elif (total == 0.0) & (newString != ""):
        print ("The list you entered is of string type only.")
        print("New string: " + newString)

typeList([2,3,1,7,4,12])
typeList(['magical','unicorns'])
typeList(['magical unicorns',19,'Hello',98.98,'world'])
