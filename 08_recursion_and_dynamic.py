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


# 8.4 power set
def get_all_subsets(s, i=None):
    if i == -1:     # last recursive call
        return [[]]
    if i is None:   # first call
        i = len(s) - 1
    
    smaller_subs = get_all_subsets(s, i-1)
    new_subs = []
    new_item = s[i]
    for _set in smaller_subs:
        new_subs.append(_set)
        new_set = _set[:]
        new_set.append(new_item)
        new_subs.append(new_set)
    return new_subs


# 8,5 recursive multiply
# O(n) solution
def recursive_multiply_a(a, b):
    if b == 0:
        return 0
    return a + recursive_multiply_a(a, b-1)

# O(log n) solution
def recursive_multiply_b(a, b, i=None):
    if i is None:
        i = b.bit_length() - 1
        
    if i == 0:
        if get_bit(b, i):
            return a
        else:
            return 0
            
    if get_bit(b, i):
        return (a << i) + recursive_multiply_b(a, b, i-1)
    else:
        return recursive_multiply_b(a, b, i-1)

def get_bit(num, i):
    mask = 1 << i
    return (num & mask) != 0


# 8.6 'towers of hanoi'
def hanoi(from_, via, to, n=None):
    if n is None:
        n = from_.size()
    if n == 1:
        to.push(from_.pop())
        return

    hanoi(from_=from_, via=to, to=via, n=n-1)
    to.push(from_.pop())
    hanoi(from_=via, via=from_, to=to, n=n-1)

from data_structures.stack import Stack
a = Stack()
a.push(5)
a.push(4)
a.push(3)
a.push(2)
a.push(1)
b = Stack()
c = Stack()
hanoi(from_=a, via=b, to=c)