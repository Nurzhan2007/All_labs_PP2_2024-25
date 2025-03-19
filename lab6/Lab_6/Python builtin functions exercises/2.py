def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print(f"String: {s}\nUppercase letters: {upper}, Lowercase letters: {lower}")
    return upper, lower

count_case("Hello World!")
