import os
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print(f"Deleted file: {path}")
        return True
    print(f"Failed to delete {path}. It may not exist or be inaccessible.")
    return False

delete_file("copy_test.txt")