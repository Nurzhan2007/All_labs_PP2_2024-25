import time
import math
def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay} milliseconds is {result}")
    return result

delayed_sqrt(25100, 2123)