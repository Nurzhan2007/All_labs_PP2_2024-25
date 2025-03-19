import re
# 8. Разделить строку по заглавным буквам
def split_by_uppercase(string):
    return re.findall(r'[A-Z][^A-Z]*', string)

print(split_by_uppercase("ThisIsATest"))  # ['This', 'Is', 'A', 'Test']