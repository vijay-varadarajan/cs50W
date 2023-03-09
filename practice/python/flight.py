class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def addpassengers(self, name):
        if not self.openseats():
            return False
        self.passengers.append(name)
        return True

    def openseats(self):
        return self.capacity - len(self.passengers)


flight = Flight(5)
people = ["A", "B", "C", "D", "E", "F"]
for person in people:
    if flight.addpassengers(person):
        print(f"Success. Added person {person}")
    else:
        print(f"Failed to add {person}")