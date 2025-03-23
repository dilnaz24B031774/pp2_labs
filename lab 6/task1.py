import os

def list_contents(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_items = os.listdir(path)

    print("Directories:", directories)
    print("Files:", files)
    print("All items:", all_items)

list_contents('pp2_labs')