dictionary = {
    "name": "Matt",
    "favorite color": "black",
    "favorite car": "my STI",
    "last name": "a short one"
}

def printdict(dict):
    for key,data in dict.iteritems():
        print "My",key,"is",data
printdict(dictionary)
