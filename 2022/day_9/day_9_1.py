file = open('input.txt', 'r')
lines = file.readlines()

head = [0,0]
tail = [0,0]

def move_head(head, direction):
    x = head[0]
    y = head[1]

    match direction:
        case 'R':
            x += 1
        case 'L':
            x -= 1
        case 'U':
            y += 1
        case 'D':
            y -= 1
        
    return [x, y]

def move_tail(tail, head):
    head_x = head[0]
    head_y = head[1]
    tail_x = tail[0]
    tail_y = tail[1]

    x_diff = head_x - tail_x
    y_diff = head_y - tail_y

    if x_diff > 1:
        tail_x += 1
    elif x_diff < -1:
        tail_x -= 1

    if y_diff > 1:
        tail_y += 1
    elif y_diff < -1:
        tail_y -= 1

    if abs(x_diff) + abs(y_diff) == 3:
        if abs(y_diff) > abs(x_diff):
            if x_diff > 0:
                tail_x += 1
            elif x_diff < 0:
                tail_x -= 1
        else:
            if y_diff > 0:
                tail_y += 1
            elif y_diff < 0:
                tail_y -= 1

    return [tail_x, tail_y]

tail_positions = {}
tail_positions[str(tail)] = 1

for command in lines:
    num_spaces = int(command.strip().split(' ')[1])
    direction = command.strip().split(' ')[0]

    for _ in range(num_spaces):
        head = move_head(head, direction)
        tail = move_tail(tail, head)
        tail_positions[str(tail)] = 1

print(f'num_of_positions: {len(tail_positions.keys())}')