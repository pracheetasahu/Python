class Temperature:
    unit = "Celsius"

    def __init__(self, value):
        self.value = value

    @staticmethod
    def is_valid(value):
        return value >= -273.15

    @classmethod
    def change_unit(cls, new_unit):
        cls.unit = new_unit

    def display(self):
        print("Temperature:", self.value, self.unit)

temp = Temperature(30)
temp.display()
print("Valid Temperature:", Temperature.is_valid(30))
Temperature.change_unit("Degree Celsius")
temp.display()
