import os
def path_info(path):
    if os.path.exists(path):
        result = {
            "filename": os.path.basename(path),
            "directory": os.path.dirname(path)
        }
        print(f"Path info for {path}: {result}")
        return result
    print(f"Path {path} does not exist.")
    return None

path_info("example.txt")