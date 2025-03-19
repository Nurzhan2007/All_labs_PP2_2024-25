import re
# 7. Snake_case -> CamelCase
def snake_to_camel(string):
    return ''.join(word.capitalize() for word in string.split('_'))

print(snake_to_camel("hello_world"))  # 'HelloWorld'