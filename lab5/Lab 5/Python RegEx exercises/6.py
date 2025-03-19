import re
# 6. Заменить пробелы, запятые, точки на ':'
def replace_special_chars(string):
    return re.sub(r'[ ,.]', ':', string)

print(replace_special_chars("Hello, world. How are you?"))  # 'Hello:world:How:are:you:'