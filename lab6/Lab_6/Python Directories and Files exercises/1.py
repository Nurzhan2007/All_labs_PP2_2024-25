import os
def list_contents(path):
    result = {
        "directories": [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))],
        "files": [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))],
        "all": os.listdir(path)
    }
    print(f"Contents of {path}: {result}")
    return result

list_contents(".")