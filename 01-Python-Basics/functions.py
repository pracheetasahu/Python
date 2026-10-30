def calculate_area(length, breadth):
    return length * breadth


def calculate_perimeter(length, breadth):
    return 2 * (length + breadth)


def display_result(area, perimeter):
    print("Area:", area)
    print("Perimeter:", perimeter)


l = 12
b = 8

print("Rectangle Measurements")
display_result(
    calculate_area(l, b),
    calculate_perimeter(l, b)
)
