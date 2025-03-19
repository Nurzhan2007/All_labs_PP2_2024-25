import math
def regular_polygon_area(sides, length):
    return (sides * length ** 2) / (4 * math.tan(math.pi / sides))

sides = int(input("Введите количество сторон: "))
length = float(input("Введите длину стороны: "))
print("Площадь многоугольника:", regular_polygon_area(sides, length))
