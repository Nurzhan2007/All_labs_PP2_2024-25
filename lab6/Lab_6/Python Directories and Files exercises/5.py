import os
def write_list_to_file(filename, lst):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines("\n".join(lst))
    print(f"List written to {filename}: {lst}")

write_list_to_file("test.txt", ["Hello", "World", "Python"])
