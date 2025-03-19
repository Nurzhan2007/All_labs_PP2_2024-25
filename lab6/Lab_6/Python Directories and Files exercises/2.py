import os
def check_access(path):
    result = {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }
    print(f"Access permissions for {path}: {result}")
    return result

check_access(".")