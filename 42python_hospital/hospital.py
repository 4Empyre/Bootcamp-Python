class Patient():
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bednumber = 0

class Hospital():
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.bedassign = 1
    def admit(self, patient):
        if len(self.patients) >= self.capacity: # if amount of people is equal to hospital capacity...
            print "We're very sorry, but we are full. Please visit our other facility on 42nd Avenue."
        else:
            self.patients.append(patient)
            patient.bednumber = self.bedassign
            self.bedassign += 1
            print patient.name,"has been administered to the facility and given bed #",patient.bednumber
        return self
    def discharge(self, patient):
        for i in self.patients:
            if i.name == patient:
                self.patients.remove(i)
                print i.name,"has been sent home."


p1 = Patient("2679b", "Sickness B Arnold", "none")
p2 = Patient("4697a","Evyl Kenevel", "none")
h1 = Hospital("Empyre's Cure-all", 2)
h1.admit(p1).admit(p2).discharge("Evyl Kenevel")
