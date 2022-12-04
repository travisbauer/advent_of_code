f = open("input.txt", "r")
rucksacks = f.read().split("\n")

priority_sum = 0

alphabet_1 = "abcdefghijklmnopqrstuvwxyz"
alphabet_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

priority_dict = {}

for i, letter in enumerate([char for char in alphabet_1 + alphabet_2]):
    priority_dict[letter] = i + 1

def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def toCharList(str):
    return [char for char in str] 

for elf_group in divide_chunks(rucksacks, 3):
    elf_group_list = []
    
    for elf in elf_group:
        elf_group_list.append(toCharList(elf))

    shared_item = list(set(elf_group_list[0]).intersection(elf_group_list[1]).intersection(elf_group_list[2]))[0]
    priority_sum += priority_dict[shared_item]

print(f'overall priority: {priority_sum}')
