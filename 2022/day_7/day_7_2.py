import re

file = open('input.txt', 'r')
lines = file.readlines()

total_size = 0

class Dir:
    def __init__(self, parent_dir, name):
        self.name = name
        self.directories = []
        self.file_sizes = []
        self.parent_dir = parent_dir

def get_dir_size(dir):
    size = sum(dir.file_sizes)

    for d in dir.directories:
        size += get_dir_size(d)

    return size

def get_req_file_size(dir, file, space_required):
    size = sum(dir.file_sizes)

    for d in dir.directories:
        size += get_req_file_size(d, file, space_required)

    if size >= space_required and size < file["size"]:
        file["size"] = size

    return size

top_dir = Dir(None, "/")
current_dir = top_dir

for line in lines:
    if 'cd' in line[0:4]:
        cd_command = re.search('\$ cd (.*)', line).group(1)
        dir = re.search('([a-z]*)', cd_command).group(1)

        if dir != '':
            new_dir = Dir(current_dir, dir)
            current_dir.directories.append(new_dir)
            current_dir = new_dir
        elif cd_command == '..':
            current_dir = current_dir.parent_dir
    else:
        file_size = re.search('(\d*)', line).group(1)

        if file_size:
            current_dir.file_sizes.append(int(file_size))

file = { "size": 70000000 }

total_size = get_dir_size(top_dir)
unused_space = 70000000 - total_size
space_required = 30000000 - unused_space

get_req_file_size(top_dir, file, space_required)

print(f'total_size: {total_size}')
print(f'space_required: {space_required}')

print(f'file_size: {file}')
