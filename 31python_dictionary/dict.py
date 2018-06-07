my_dict = {
    "name": "Matt",
    "age": 32,
    "country of birth": "The United States",
    "favorite language": "Python"
}

def printdict(dict):
    for key,data in dict.iteritems():
        print "My",key,"is",data

printdict(my_dict)
