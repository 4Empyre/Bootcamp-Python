# PART 1
print("PART 1")
def draw_stars(nums):
    for x in nums:
        print "*"*x
draw_stars([4,6,1,3,5,7,25])

# PART 2
print("PART 2")
def drawing_stars(list_one):
    for x in list_one:
        if isinstance(x, int):
            print "*"*x
        elif isinstance(x, str):
            print (x.lower()[0])*len(x)
drawing_stars([5,12,31,"Matt",13,"Makes",42,"Moooooooooooooore"])
