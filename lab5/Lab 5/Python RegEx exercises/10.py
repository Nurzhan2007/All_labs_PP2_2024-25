import re
# 10. CamelCase -> snake_case
def camel_to_snake(string):
    return re.sub(r'([A-Z])', r'_\1', string).lower().lstrip('_')

print(camel_to_snake("CamelCaseString"))  # 'camel_case_string'