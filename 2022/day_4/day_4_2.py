f = open("input.txt", "r")
assignments = f.read().split("\n")

num_pairs = 0

for pair in assignments:
    pair_1 = list(range(int(pair.split(',')[0].split("-")[0]), int(pair.split(',')[0].split("-")[1]) + 1))
    pair_2 = list(range(int(pair.split(',')[1].split("-")[0]), int(pair.split(',')[1].split("-")[1]) + 1))

    if len(list(set(pair_1).intersection(pair_2))) > 0:
        num_pairs += 1

print(f'num_pairs: {num_pairs}')
