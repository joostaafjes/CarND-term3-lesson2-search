# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid, goal, cost):

    value_matrix = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]

    open_list = []
    open_list.append([0, goal[0], goal[1]])

    while len(open_list) > 0:
        open_list.sort()
        open_list.reverse()
        node = open_list.pop()
        value = node[0]
        y = node[1]
        x = node[2]
        value_matrix[y][x] = value
        for i in range(len(delta)):
            y2 = y + delta[i][0]
            x2 = x + delta[i][1]
            if y2 >= 0 and y2 < len(grid) and x2 >= 0 and x2 < len(grid[0]):
                if grid[y2][x2] == 0 and value_matrix[y2][x2] == 99:
                    open_list.append([value + cost, y2, x2])

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    return value_matrix

value_grid = compute_value(grid, goal, cost)

for row in value_grid:
    print(row)