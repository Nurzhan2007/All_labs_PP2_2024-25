import os
def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        line_count = sum(1 for _ in file)
    print(f"File {filename} has {line_count} lines.")
    return line_count

write_list_to_file("test.txt", ["Hello", "World", "Python"])
count_lines("test.txt")
