file = open('input.txt', 'r')
instructions = file.readlines()

cpu = {}
cpu['register'] = 1
cpu['cycle'] = 0
cpu["current_line"] = ""
cpu['display'] = []

def print_pixel(cpu):
    cycle = cpu['cycle'] - 1
    
    if (cycle <= (cpu['register'] + 1) and cycle >= (cpu['register'] - 1)):
        cpu["current_line"] += '#'
    else:
        cpu["current_line"] += '.'

    if cpu['cycle'] % 40 == 0:
        cpu['display'].append(cpu["current_line"])
        cpu["current_line"] = ""
        cpu['cycle'] -= 40

def addx(cpu, v):
    for _ in range(2):
        cpu['cycle'] += 1
        print_pixel(cpu)

    cpu['register'] += v

def noop(cpu):
    cpu['cycle'] += 1
    print_pixel(cpu)

for instruction in instructions:
    if instruction.strip() == "noop":
        noop(cpu)
    else:
        addx(cpu, int(instruction.split(' ')[1]))

for line in cpu["display"]:
    print(line)
