from instance_methods_example import Flight


class CommercialFlight(Flight):
    def __init__(self, operator, destination, passengers):
        super().__init__(operator, destination)
        self.passengers = passengers

    def startboarding(self, ready):
        if ready:
            return f"{self.passengers} passengers can start boarding on {self}"
        else:
            return f"No boarding yet for {self}"


# Instantiating objects
c = CommercialFlight("Virgin", "Copenhagen", 120)

print(c.startboarding(True))
print(c.takeoff(True))
