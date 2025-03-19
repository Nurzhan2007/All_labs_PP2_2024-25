import re
# 3. Последовательности строчных букв, соединенные '_'
def match_lowercase_underscore(string):
    return bool(re.fullmatch(r'[a-z]+_[a-z]+', string))

print(match_lowercase_underscore("hello_world"))  # True