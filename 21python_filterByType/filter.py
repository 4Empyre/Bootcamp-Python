def filter(x): # creates a function to be used on any list
    if isinstance(x, list): # check if x is a list
        if len(x) >= 10:
            print "Big list!"
        elif len(x) < 10:
            print "Short list."
    elif isinstance(x, int): # check if x is an integer
        if x >= 100:
            print "That's a big number!"
        elif x < 100:
            print "That's a small number"
    elif isinstance(x, str): # check if x is a string
        if len(x) >= 50:
            print "Long sentence."
        elif len(x) < 50:
            print "Short sentence."
    else:
        print "We have a problem!"
