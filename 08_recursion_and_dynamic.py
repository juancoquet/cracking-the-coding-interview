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

# 8.7 'permutations without dups'
def permutations(string):
    if len(string) == 1:
        return [string]
    
    smaller_perms = permutations(string[:-1])
    results = []
    new_char = string[-1]
    for perm in smaller_perms:
        length = len(perm)
        for i in range(length):
            left = perm[:i]
            right = perm[i:]
            result = left + new_char + right
            results.append(result)
        results.append(perm + new_char)

    return results


# 8.8 'permutations without dups'
class PrefixTree:

    def __init__(self, key=None):
        self.key = key
        self.children = {}

    def _add_child(self, key):
        if key not in self.children:
            self.children[key] = PrefixTree(key)

    def build_prefixes(self, string):
        if len(string) > 0:
            chars = list(string)
            for c in chars:
                self._add_child(c)
    
            for key, child in self.children.items():
                remaining = chars[:]
                remaining.remove(key)
                remaining = ''.join(remaining)
                child.build_prefixes(remaining)

    def read_permutations(self, permutation=''):
        if self.key is not None:
            permutation += self.key
            
        if len(self.children) == 0:
            print(permutation)
            return
            
        for child in self.children.values():
            child.read_permutations(permutation)

# 8.10 'paint fill'
def paint_fill(start, new_color, screen):
    num_rows = len(screen)
    num_cols = len(screen[0])
    deltas = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]
    r, c = start
    orig_color = screen[r][c]
    
    to_visit = [start]
    while len(to_visit) > 0:
        curr = to_visit.pop(0)
        r, c = curr
        screen[r][c] = new_color
        for d in deltas:
            r_delta, c_delta = d
            check_r = r + r_delta
            check_c = c + c_delta
            if 0 <= check_r < num_rows and 0 <= check_c < num_cols:
                if screen[check_r][check_c] == orig_color:
                    to_visit.append((check_r, check_c))


# 8.11 'coins'
def simplest_change(n):
    change = {
        25: 0,
        10: 0,
        5: 0,
        1: 0
    }
    while n >= 25:
        change[25] += 1
        n -= 25
    while n >= 10:
        change[10] += 1
        n -= 10
    while n >= 5:
        change[5] += 1
        n -= 5
    while n:
        change[1] += 1
        n -= 1
    return change

def generate_combinations(change, combos=[]):
    combos += [change]
    if not (change[25] or change[10] or change[5]):
        return combos
    if change[5]:
        new_combo = change.copy()
        new_combo[5] -= 1
        new_combo[1] += 5
        combos = generate_combinations(new_combo, combos)
    if change[10]:
        new_combo = change.copy()
        new_combo[10] -= 1
        new_combo[5] += 2
        combos = generate_combinations(new_combo, combos)
    if change[25]:
        new_combo = change.copy()
        new_combo[25] -= 1
        new_combo[10] += 2
        new_combo[5] += 1
        combos = generate_combinations(new_combo, combos)
    return combos

def coins(n):
    simplest = simplest_change(n)
    return generate_combinations(simplest)