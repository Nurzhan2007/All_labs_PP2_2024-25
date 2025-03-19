import re
# 9. Вставить пробелы перед словами, начинающимися с заглавных
def insert_spaces(string):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', string)

print(insert_spaces("camelCaseString"))  # 'camel Case String'
