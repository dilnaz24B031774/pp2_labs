def copy_file(source, destination):
    try:
        with open(source, 'r') as src, open(destination, 'w') as dest:
            dest.write(src.read())
        print("File copied successfully")
    except FileNotFoundError:
        print("Source file not found")

copy_file('pp2_labs/lab 6/source.txt', 'pp2_labs/lab 6/destination.txt')
