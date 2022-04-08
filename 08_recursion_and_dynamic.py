# 8.2 robot in a grid
def get_path(maze):
    path = []
    last_row = len(maze) - 1
    last_col = len(maze[0]) - 1
    if path_exists(maze, last_row, last_col, path):
        return path
    return None

def path_exists(maze, target_row, target_col, path):
    # check maze boundaries and availability of current cell
    if target_row < 0 or target_col < 0 or not maze[target_row][target_col]:
        return False
    is_at_origin = (target_row == 0) and (target_col == 0)

    # recursive step. check if path exists to neighbours. if path exists to sequence of neighbours leading back to origin, add this cell to path.
    if (
        is_at_origin
        or path_exists(maze, target_row, target_col-1, path) # check western neighbour
        or path_exists(maze, target_row-1, target_col, path) # check northern neighbour
    ):
        cell = (target_row, target_col)
        path.append(cell)
        return True

    return False

# 8.3 magic index
def magic_index(a, left_i=0):
    if len(a) < 1:
        return None
    midpoint = len(a) // 2
    i = midpoint + left_i
    if a[midpoint] == i:
        return i
    elif a[midpoint] > i:
        return magic_index(a[:midpoint], left_i=left_i)
    else:
        return magic_index(a[midpoint+1:], left_i=i+1)


a = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]

print(magic_index(a))