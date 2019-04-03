# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. Note that the 'v' should be
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------
import copy

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid, init, goal, cost):
    def get_list_from_node(current_node, grid, g, cost, expand):
        # search all options for 1 node and return list of found nodes
        new_list = []
        exp_list = []
        y = current_node[1]
        x = current_node[2]
        for step in range(len(delta)):
            new_y = y + delta[step][0]
            new_x = x + delta[step][1]
            if new_y < 0 or new_y > (len(grid) - 1) or \
                    new_x < 0 or new_x > (len(grid[0]) - 1):
                continue
            if grid[new_y][new_x] == 1:
                continue
            expand_copy = copy.deepcopy(expand)
            expand_copy[y][x] = delta_name[step]
            exp_list.append(expand_copy)
            new_list.append([g + cost, new_y, new_x])
        grid[y][x] = 1

        return new_list, exp_list

    def extend_list(list, extend_list, expand_list, extend_expand_list):
        # if node already exists with x and y, take the one with the lowest g value
        if len(list) == 0:
            list = extend_list
            expand_list = extend_expand_list
        else:
            for ext_count in range(len(extend_list)):
                found = False
                for count in range(len(list)):
                    if list[count][1] == extend_list[ext_count][1] and list[count][2] == extend_list[ext_count][2]:
                        if list[count][0] > extend_list[ext_count][0]:
                            list[count][0] = extend_list[ext_count][0]
                            expand_list[count] = extend_expand_list[ext_count]
                        found = True
                        continue
                if not found:
                    list.append(extend_list[ext_count])
                    expand_list.append(extend_expand_list[ext_count])

        return list, expand_list

    # search in grid until goal is reached
    g = 0
    list = []
    list.append([g, init[0], init[1]])
    expand = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    expand_list = [expand]
    while len(list) > 0 and not(list[0][1] == goal[0] and list[0][2] == goal[1]):
        new_list = []
        new_expand_list = []
        for count in range(len(list)):
            current_node = list[count]
            [ext_list, ext_expand] = get_list_from_node(current_node, grid, current_node[0], cost, expand_list[count])
            [new_list, new_expand_list] = extend_list(new_list, ext_list, new_expand_list, ext_expand)
        list = new_list
        expand_list = new_expand_list

    if len(list) == 1:
        expand = expand_list[0]
        expand[goal[0]][goal[1]] = "*"
        return expand
    else:
        return 'fail'

found_grid = search(grid, init, goal, cost)

for row in found_grid:
    print(row)
