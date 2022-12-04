f = open("input.txt", "r")
rucksacks = f.read().split("\n")

priority_sum = 0

alphabet_1 = "abcdefghijklmnopqrstuvwxyz"
alphabet_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

priority_dict = {}

for i, letter in enumerate([char for char in alphabet_1 + alphabet_2]):
    priority_dict[letter] = i + 1

for rucksack in rucksacks:
    items = [char for char in rucksack]   
    middle_index = len(items) // 2
    compartment_1 = items[:middle_index]
    compartment_2 = items[middle_index:]

    shared_item = list(set(compartment_1).intersection(compartment_2))[0]

    priority_sum += priority_dict[shared_item]

print(f'overall priority: {priority_sum}')