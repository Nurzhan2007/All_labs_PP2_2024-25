import re
# 4. Одна заглавная буква, затем строчные
def match_upper_lower(string):
    return bool(re.fullmatch(r'[A-Z][a-z]+', string))

print(match_upper_lower("Hello"))  # True