file = open('input.txt', 'r')
lines = file.readlines()

matrix = []

for line in lines:
    matrix_list = []

    for tree_height in line.strip():
        matrix_list.append(tree_height)
    
    matrix.append(matrix_list)

def trees_to_check(tree, a, b, x, y):
    tree_cordinates = []
    for i in range(a, b):
        if x != None:
            if i + tree[1] != tree[1]:
                tree_cordinates.append([x, i + tree[1]])
        if y != None:
            if i + tree[0] != tree[0]:
                tree_cordinates.append([i + tree[0], y])
    return tree_cordinates

def is_tree_visible(tree_x, tree_y, tree_matrix):
    max_x = len(tree_matrix)
    max_y = len(tree_matrix[0])
    tree_height = tree_matrix[tree_x][tree_y]

    tree_cordinates = {}

    tree_cordinates["down"] = trees_to_check([tree_x, tree_y], 0, max_y - tree_y, tree_x, None)
    tree_cordinates["up"] = trees_to_check([tree_x, tree_y], 0 - tree_y, 0, tree_x, None)

    tree_cordinates["right"] = trees_to_check([tree_x, tree_y], 0, max_x - tree_x, None, tree_y)
    tree_cordinates["left"] = trees_to_check([tree_x, tree_y], 0 - tree_x, 0, None, tree_y)

    is_visible = False
    for direction in tree_cordinates.keys():
        blocking_tree = False
        for dirction_cordinate in tree_cordinates[direction]:
            if tree_matrix[dirction_cordinate[0]][dirction_cordinate[1]] >= tree_height:
                blocking_tree = True

        if blocking_tree == False:
            is_visible = True
            break

    return is_visible

max_x = len(matrix)
max_y = len(matrix[0])

visible_trees = max_x * 2 + max_y * 2 - 4

for x in range(1, max_x - 1):
    for y in range(1, max_y - 1):
        if is_tree_visible(x, y, matrix):
            visible_trees += 1

print(visible_trees)