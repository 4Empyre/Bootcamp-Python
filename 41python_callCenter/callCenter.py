class Call():
    def __init__(self, id, callername, callerphonenumber, timeofcall, reasonforcall):
        self.id = id
        self.name = callername
        self.number = callerphonenumber
        self.time = timeofcall
        self.reason = reasonforcall
    def display(self):
        print "Id:",self.id
        print "Caller name:",self.name
        print "Caller phone number:",self.number
        print "Time of call:",self.time
        print "Reason for call:",self.reason
call1 = Call("27692b","Jessica","(555)555-5556","4:20","Defective product")
call2 = Call("26592a","Robert","(666)666-6666)","4:34","Unhappy with product quality")
# call1.display() # for testing

class CallCenter():
    def __init__(self):
        self.calls = []
        self.queue = len(self.calls)
    def info(self):
        for x in self.calls:
            print x.name,x.number
        return self
    def add(self, call):
        self.calls.append(call)
        return self
    def remove(self):
        del self.calls[0]
        return self

EmpyreCallCenter = CallCenter()
EmpyreCallCenter.add(call1).add(call2).info().remove().info()
