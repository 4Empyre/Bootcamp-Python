def odd_even():
    for i in range(1, 2001):
        if i % 2 != 0:
            print("Number is " + str(i) + ". This is an odd number.")
        elif i % 2 == 0:
            print("Number is " + str(i) + ". This is an even number.")
#odd_even()


def multiply(arr, y):
    new_list = []
    for i in arr:
        new_list.append(i*y)
    return new_list
a = [2,4,10,16]
b = multiply(a, 5)
#print b

# INCOMPLETE
# Answer should looks like [[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
def layered_multiples(arr):
    new_array = []
    final_array = []
    for i in arr:
        new_array

        print final_array
    return final_array
x = layered_multiples(multiply([2,4,5],3))
print x
