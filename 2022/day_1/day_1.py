f = open("input.txt", "r")
calorie_list = f.read().split("\n")

elf_count = 0
elf_calories = 0
calories_per_elf = {}
total_calories = 0

for calories in calorie_list:
    if calories == '':
        calories_per_elf[elf_count] = elf_calories
        elf_calories = 0
        elf_count += 1
    else:
        elf_calories += int(calories)

print(f'Highest Value Elf: {max(calories_per_elf.values())}')

for _ in range(3):
    calories = max(calories_per_elf.values())
    total_calories += calories
    key_list = list(calories_per_elf.keys())
    val_list = list(calories_per_elf.values())
    position = val_list.index(calories)
    calories_per_elf.pop(key_list[position])

print(f'Top Three Elves Sum: {total_calories}')
