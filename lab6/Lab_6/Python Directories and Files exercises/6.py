import os
def generate_files():
    for char in range(ord('A'), ord('Z') + 1):
        filename = f"{chr(char)}.txt"
        with open(filename, 'w') as file:
            file.write(f"File {chr(char)}.txt")
        print(f"Created file: {filename}")

generate_files()