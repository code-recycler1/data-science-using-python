class Flight:
    airport = "Brussels South"  # Class attribute

    def __init__(self, operator, destination):
        self.operator = operator  # Instance attribute
        self.destination = destination  # Instance attribute


# Instantiating objects
a = Flight("Virgin", "Amsterdam")
b = Flight("Ryanair", "Berlin")

print('From', a.airport, "to", a.destination)
print('From', b.airport, "to", b.destination)
