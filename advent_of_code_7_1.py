class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name, parent_dir):
        self.name = name
        self.parent_dir = parent_dir
        self.files = []
        self.total_size = 0


f = open(r'C:\Users\alanp\git\advent_of_code_2022\advent_of_code_7_input.txt')
content = f.readlines()
current_dir_stack = []
directories = []

root_dir = Directory('/', '')
directories.append(root_dir)
print(f'Adding directory {root_dir.name}, parent is {root_dir.parent_dir}')

for line in content:
    line = line.replace('\n', '')
    print(f'** {line}')
    if line[0:4] == "$ cd":
        command_parts = line.split(' ')
        if command_parts[2] != "..":
            current_dir_stack.append(command_parts[2])
            print(f'Changed current dir to {"/".join(current_dir_stack)}')
        else:
            current_dir_stack.pop()
    elif line[0:4] == "$ ls":
        pass
    elif line[0:3] == "dir":
        output_parts = line.split(' ')
        dir_exists = False
        for dir in directories:
            if dir.name == '/'.join(current_dir_stack) + '/' + output_parts[1]:
                dir_exists = True
                break
        if not dir_exists:
            dir_name = '/'.join(current_dir_stack) + '/' + output_parts[1]
            directory = Directory(dir_name, '/'.join(current_dir_stack))
            print(f'Adding directory {dir_name}, parent is {"/".join(current_dir_stack)}')
            directories.append(directory)
    else:
        output_parts = line.split(' ')
        file = File(output_parts[1], int(output_parts[0]))
        for dir in directories:
            if dir.name == '/'.join(current_dir_stack):
                dir.files.append(file)
                print(f'Adding file {file.name}, {file.size} bytes to directory {dir.name}')
                dir.total_size = dir.total_size + file.size
                print(f'Directory {dir.name} total size increased to {str(dir.total_size)} bytes')
                next_dir_name = dir.parent_dir
                while next_dir_name != '':
                    for parent_dir in directories:
                        if parent_dir.name == next_dir_name:
                            parent_dir.total_size = parent_dir.total_size + file.size
                            print(f'Directory {parent_dir.name} total size increased to {str(parent_dir.total_size)} bytes')
                            next_dir_name = parent_dir.parent_dir
                            print(f'Looking for parent {next_dir_name}')
                            break
                break

total_size = 0
for dir in directories:
    if dir.total_size <= 100000:
        total_size = total_size + dir.total_size

print(total_size)
    