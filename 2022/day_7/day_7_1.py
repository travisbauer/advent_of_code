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

def get_dir_size(dir, totals):
    size = sum(dir.file_sizes)

    for d in dir.directories:
        size += get_dir_size(d, totals)

    if size <= 100000:
        totals["sum"] += size

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

totals = { "sum": 0 }

get_dir_size(top_dir, totals)
print(f'total_sum: {totals["sum"]}')
