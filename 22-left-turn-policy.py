# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1, 0],  # go up
           [0, -1],  # go left
           [1, 0],  # go down
           [0, 1]]  # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]

cost = [2, 1, 20]  # cost has 3 values, corresponding to making


# a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid, init, goal, cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
    actions = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
               [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
               [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
               [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for f in range(len(forward)):
                    if x == init[0] and y == init[1] and f != init[2]:
                        continue
                    xp = x - forward[f][0]
                    yp = y - forward[f][1]
                    if goal[0] == x and goal[1] == y and \
                            xp >= 0 and xp < len(grid) and yp >= 0 and yp < len(grid[0]) and grid[xp][yp] == 0:
                        if value[f][x][y] > 0:
                            value[f][x][y] = 0
                            change = True

                    elif grid[x][y] == 0:
                        for a in range(len(action)):
                            f2 = (f + action[a]) % 4
                            x2 = x + forward[f2][0]
                            y2 = y + forward[f2][1]

                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0 and \
                                    (xp >= 0 and xp < len(grid) and yp >= 0 and yp < len(grid[0]) and grid[xp][
                                        yp] == 0 or \
                                     x == init[0] and y == init[1] and f == init[2]):
                                v2 = value[f2][x2][y2] + cost[a]

                                if v2 < value[f][x][y]:
                                    change = True
                                    value[f][x][y] = v2
                                    actions[f][x][y] = a
                                    # if v2 == min(value[0][x][y], value[1][x][y], value[2][x][y], value[3][x][y]):
                                    # policy[x][y] = action_name[a]

    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    x = init[0]
    y = init[1]
    f = init[2]

    while not (x == goal[0] and y == goal[1]):
        act = actions[f][x][y]
        policy[x][y] = action_name[act]

        f = (f + action[act]) % 4
        x = x + forward[f][0]
        y = y + forward[f][1]
    policy[goal[0]][goal[1]] = '*'

    return policy

value_grid = optimum_policy2D(grid, init, goal, cost)

for row in value_grid:
    print(row)
