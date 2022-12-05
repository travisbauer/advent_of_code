import re

file1 = open('input.txt', 'r')
Lines = file1.readlines()

def generateStacks(lines):
    stackLines = []
    instructions = []
    isStack = True

    for line in lines:
        if line == '\n':
            isStack = False
        elif isStack:
            stackLines.append(line)
        else: 
            instructions.append(line)

    stackLines.reverse()
    stackLines.pop(0)

    stacks = {}
    num_stacks = int(len(stackLines[0]) / 4)

    for i in range(num_stacks):
        stacks[i + 1] = []

    for line in stackLines:
        lineStack = [line[i:i+4].strip() for i in range(0, len(line), 4)]
        for i, crate in enumerate(lineStack):
            if crate != '':
                stacks[i + 1].append(crate.replace('[', '').replace(']', ''))

    return stacks, instructions

stacks, instructions = generateStacks(Lines)

for instruction in instructions:
    regexPattern = 'move (.+?) from (.+?) to (.+?)'
    num_to_move = int(re.search(regexPattern, instruction).group(1))
    from_idx = int(re.search(regexPattern, instruction).group(2))
    to_idx = int(re.search(regexPattern, instruction).group(3))

    for _ in range(num_to_move):
        stacks[to_idx].append(stacks[from_idx].pop())

top_stack = ""
for stack in stacks.values():
    top_stack += stack[-1]

print(f'top of stack: {top_stack}')
