import re
# 5. 'a' с любым текстом, заканчивающимся 'b'
def match_a_anything_b(string):
    return bool(re.fullmatch(r'a.*b', string))

print(match_a_anything_b("a123b"))  # True