import math
def parallelogram_area(base, height):
    return base * height

base = float(input("Введите длину основания параллелограмма: "))
height = float(input("Введите высоту параллелограмма: "))
print("Площадь параллелограмма:", parallelogram_area(base, height))
