import os
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"Deleted: {path}")
        else:
            print("No write permission")
    else:
        print("File does not exist")
delete_file('pp2_labs/sample.txt')  
