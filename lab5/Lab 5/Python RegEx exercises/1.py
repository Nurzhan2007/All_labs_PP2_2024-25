import re
# 1. 'a' с 0 или более 'b'
def match_a_b(string):
    return bool(re.fullmatch(r'a[b]*', string))

print(match_a_b("abbb"))  # True