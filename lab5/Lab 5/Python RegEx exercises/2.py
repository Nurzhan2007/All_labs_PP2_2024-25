import re
# 2. 'a' с 2 или 3 'b'
def match_a_bb(string):
    return bool(re.fullmatch(r'a[b]{2,3}', string))

print(match_a_bb("abb"))  # True