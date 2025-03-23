def write_list_to_file(filename, items):
    with open(filename, 'w') as file:
        for item in items:
            file.write(str(item) + '\n')
write_list_to_file('output.txt', ['computer', 'TV', 'phone','tablet'])

