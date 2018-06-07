# PART 1 complete
"""
class MathDojo(object):
    def __init__(self):
        self.total = 0
    def add(self, num1, *nums):
        self.total += num1
        if nums:
            for i in nums:
                self.total += i
        return self
    def subtract(self, num1, *nums):
        self.total -= num1
        if nums:
            for i in nums:
                self.total -= i
        return self
    def result(self):
        print self.total

md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result() # for testing
"""
# PART 2 complete
# Modify MathDojo to take at least one integer and/or list as a parameter with any number for values passed into the list.

class MathDojo(object):
    def __init__(self,):
        self.total = 0
    def add(self, num, *nums):
        if type(num) == list:
            for i in num:
                self.total += i
        elif type(num) == int:
            self.total += num
        if nums:
            for i in nums:
                if type(i) == list:
                    for x in i:
                        self.total += x
                elif type(i) == int:
                    self.total += i
        return self
    def subtract(self, num, *nums):
        if type(num) == list:
            for i in num:
                self.total -= i
        elif type(num) == int:
            self.total -= num
        if nums:
            for i in nums:
                if type(i) == list:
                    for x in i:
                        self.total -= x
                elif type(i) == int:
                    self.total -= i
        return self
    def result(self):
        print self.total

md = MathDojo()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
