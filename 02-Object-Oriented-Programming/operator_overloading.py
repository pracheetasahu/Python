class Distance:
    def __init__(self, meters):
        self.meters = meters

    def __add__(self, other):
        return Distance(self.meters + other.meters)

    def __str__(self):
        return str(self.meters) + " meters"

d1 = Distance(500)
d2 = Distance(750)
d3 = d1 + d2

print("First Distance:", d1)
print("Second Distance:", d2)
print("Total Distance:", d3)
