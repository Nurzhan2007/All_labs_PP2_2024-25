import shutil
def copy_file(src, dst):
    shutil.copy(src, dst)
    print(f"Copied content from {src} to {dst}")

copy_file("test.txt", "copy_test.txt")
