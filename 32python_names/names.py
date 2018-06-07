# PART 1
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def names(list):
    for x in list:
        print x["first_name"], x["last_name"]

# names(students)

# PART 2
users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}
def names(dict):
    print "Students"
    for x in range(0, len(dict["Students"])):
        currentUser = users['Students'][x]
        numChars = len(currentUser['first_name']) + len(currentUser['last_name'])
        print x+1,"-",currentUser['first_name'],currentUser['last_name'],"-",numChars
    print "Instructors"
    for x in range(0, len(users["Instructors"])):
        currentUser = users['Instructors'][x]
        numChars = len(currentUser['first_name']) + len(currentUser['last_name'])
        print x+1,"-",currentUser['first_name'],currentUser['last_name'],"-",numChars
names(users)
