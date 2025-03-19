import math
def multiply_list(numbers):
    result = math.prod(numbers)
    print(f"Product of {numbers} is {result}")
    return result

multiply_list([2, 3, 4])