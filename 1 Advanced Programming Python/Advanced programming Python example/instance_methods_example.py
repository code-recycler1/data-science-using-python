class Flight:
    airport = "Brussels South"

    def __init__(self, operator, destination):
        self.operator = operator
        self.destination = destination

    def __str__(self):
        return f"Flight from {self.airport} to {self.destination}"

    def takeoff(self, ready):
        if ready:
            return f"{self} ready for takeoff"
        else:
            return f"{self} still waiting"


# Instantiating objects
a = Flight("Virgin", "Amsterdam")
b = Flight("Ryanair", "Berlin")

print(a)
print(b)
print(a.takeoff(False))
print(b.takeoff(True))
