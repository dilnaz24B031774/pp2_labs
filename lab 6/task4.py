def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            print("Number of lines:", sum(1 for line in file))
    except FileNotFoundError:
        print("File not found")

count_lines('pp2_labs/lab 6/row.txt')