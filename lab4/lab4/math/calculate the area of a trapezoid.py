def trapezoid_area(height, base1, base2):
    return (base1 + base2) * height / 2

height = float(input("Введите высоту трапеции: "))
base1 = float(input("Введите первое основание: "))
base2 = float(input("Введите второе основание: "))
print("Площадь трапеции:", trapezoid_area(height, base1, base2))
