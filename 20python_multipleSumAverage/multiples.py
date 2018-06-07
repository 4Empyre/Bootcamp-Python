# Multiples
for i in range(1, 101):
    if i % 2 != 0: # finds odd numbers
        print i

for i in range(1, 1001):
    if i % 5 == 0:
        print i

# Sum list
a = [1,2,5,10,255,3]
sum = 0 # create a blank integer to add numbers into
for i in a: # for each item in a
    sum += i # add it into sum
print sum

# Average list
a = [1,2,5,10,255,3]
sum = 0
for i in a:
    sum += i # adds the entire list together into sum
average = sum / len(a) # divide sum by the amount of numbers added together to find the average
print average
