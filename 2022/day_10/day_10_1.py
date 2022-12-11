file = open('input.txt', 'r')
instructions = file.readlines()

cpu = {}
cpu['register'] = 1
cpu['cycle'] = 0
cpu['sum'] = 0

def increment_sum(cpu):
    cycle_temp = cpu['cycle'] - 20

    if cycle_temp == 0 or cycle_temp % 40 == 0:
        cpu['sum'] += cpu['register'] * cpu['cycle']

def addx(cpu, v):
    for _ in range(2):
        cpu['cycle'] += 1
        increment_sum(cpu)

    cpu['register'] += v

def noop(cpu):
    cpu['cycle'] += 1
    increment_sum(cpu)

for instruction in instructions:
    if instruction.strip() == "noop":
        noop(cpu)
    else:
        addx(cpu, int(instruction.split(' ')[1]))

print(cpu)