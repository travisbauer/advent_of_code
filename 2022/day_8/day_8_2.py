file = open('input.txt', 'r')
lines = file.readlines()

matrix = []

for line in lines:
    matrix_list = []

    for tree_height in line.strip():
        matrix_list.append(tree_height)
    
    matrix.append(matrix_list)

def trees_to_check(tree, a, b, x, y, tree_matrix):
    tree_height = tree_matrix[tree[0]][tree[1]]
    r = None

    if a == 0:
        r = range(a,b)
    else:
        r = reversed(range(a,b))

    furthest_tree = None

    for i in r:
        if x != None:
            if i + tree[1] != tree[1]:
                furthest_tree = [x, i + tree[1]]

                if tree_matrix[x][i + tree[1]] >= tree_height:
                    break;

        if y != None:
            if i + tree[0] != tree[0]:
                furthest_tree = [i + tree[0], y]

                if tree_matrix[i + tree[0]][y] >= tree_height:
                    break;
    
    return furthest_tree

def get_tree_score(tree_x, tree_y, tree_matrix):
    max_x = len(tree_matrix)
    max_y = len(tree_matrix[0])

    tree_cordinates = {}

    tree_cordinates["down"] = trees_to_check([tree_x, tree_y], 0, max_y - tree_y, tree_x, None, tree_matrix)
    tree_cordinates["up"] = trees_to_check([tree_x, tree_y], 0 - tree_y, 0, tree_x, None, tree_matrix)

    tree_cordinates["right"] = trees_to_check([tree_x, tree_y], 0, max_x - tree_x, None, tree_y, tree_matrix)
    tree_cordinates["left"] = trees_to_check([tree_x, tree_y], 0 - tree_x, 0, None, tree_y, tree_matrix)


    down = abs(tree_y - tree_cordinates["down"][1])
    up = abs(tree_y - tree_cordinates["up"][1])
    right = abs(tree_x - tree_cordinates["right"][0])
    left = abs(tree_x - tree_cordinates["left"][0])

    return down * up * right * left

max_x = len(matrix)
max_y = len(matrix[0])

max_score = 0
for x in range(1, max_x - 1):
    for y in range(1, max_y - 1):
        score = get_tree_score(x, y, matrix)
        if score > max_score:
            max_score = score

print(max_score)
