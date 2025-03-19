def all_true(t):
    result = all(t)
    print(f"Tuple: {t} all elements are true: {result}")
    return result

all_true((True, True, False))