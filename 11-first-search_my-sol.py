# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


# grid = [[0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0],
#         [0, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 1, 0]]

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]]

init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    open_list = [[0, init]]
    path = 'fail'
    while len(open_list) > 0 and \
          not(open_list[0][1][0] == goal[0] and open_list[0][1][1] == goal[1]):
        #
        # taken lowest g-Value entry
        #
        open_list.sort()
        first_entry = open_list.pop(0)
        g_value = first_entry[0]
        position = first_entry[1]

        #
        # for each delta
        #
        for delta_index in range(len(delta)):
            new_position = [position[0] + delta[delta_index][0], position[1] + delta[delta_index][1]]
            if new_position[0] < 0 or new_position[0] > len(grid) - 1 or \
               new_position[1] < 0 or new_position[1] > len(grid[0]) - 1 or \
               grid[new_position[0]][new_position[1]] != 0:
                continue;
            open_list.append([g_value + cost, new_position])
            grid[position[0]][position[1]] = 1
            # grid[new_position[0]][new_position[1]] = delta_name[delta_index]


    # if open list is goal return, otherwise return fail
    if len(open_list) > 0:
        path = [open_list[0][0], open_list[0][1][0], open_list[0][1][1]]

    return path

print(search(grid, init, goal, cost))


