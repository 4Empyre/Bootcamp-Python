# Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
words2 = words.replace("day", "month")
print words2

# Min and Max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

# First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0] # prints first
print x[len(x)-1] # prints last
x2 = [x[0], x[len(x)-1]]
print x2

# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6,]
x.sort()
print x
x1 = x[0:len(x)/2] # new list is first half of original list
print x1
x2 = x[len(x)/2:len(x)] # new list is last half of original list
print x2
x2.insert(0, x1) # insert x1 into x2 at position 0
print x2
