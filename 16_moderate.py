# solving 16.2 word frequencies
def word_freq(book):
    book = book.replace(',', '').replace('.', '').lower()
    words = book.split()
    freqs = {}
    for w in words:
        if w in freqs:
            freqs[w] += 1
        else:
            freqs[w] = 1
    return freqs


# 16.4 tic tac toe win
def tic_tac_win(board, board_size=3):
    for row in board:
        first_item = row[0]
        for item in row:
            if item != first_item:
                break
        else: # all items were the same
            return True
    
    for col in range(board_size):
        first_item = board[0][col]
        for row in board:
            if row[col] != first_item:
                break
        else: # all items were the same
            return True

    top_left = board[0][0]
    for i in range(board_size):
        if board[i][i] != top_left:
            break
    else:
        return True

    top_right = board[0][-1]
    for row, col in zip(range(board_size), range(board_size-1, -1, -1)):
        if board[row][col] != top_right:
            break
    else:
        return True
    
    return False

# 16.5 factorial zeros
def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n

def trailing_zeros(n):
    zeros = 0
    while n % 10 == 0:
        zeros += 1
        n /= 10

def factorial_zeros(n):
    fact = factorial(n)
    zeros = trailing_zeros(fact)
    return zeros


# 16.6 smallest difference
def _smallest_difference(arr, midpoint=None):
    if len(arr) > 1:
        if midpoint is None:
            midpoint = len(arr) // 2
        left = arr[:midpoint]
        right = arr[midpoint:]
        
        _smallest_difference(left)
        _smallest_difference(right)
        
        li, ri, i = 0, 0, 0
        min_diff = float('inf')
    
        while li < len(left) and ri < len(right):
            if left[li] <= right[ri]:
                arr[i] = left[li]
                li += 1
            elif left[li] > right[ri]:
                arr[i] = right[ri]
                if left[li] - right[ri] < min_diff:
                    min_diff = left[li] - right[ri]
                ri += 1
            i += 1
    
        while li < len(left):
            arr[i] = left[li]
            if left[li] - right[-1] < min_diff:
                min_diff = left[li] - right[-1]
            li += 1
            i += 1
    
        while ri < len(right):
            arr[i] = right[ri]
            ri += 1
            i += 1
    
        if min_diff == float('inf'):
            min_diff = None
    
        return min_diff

def smallest_difference(a_arr, b_arr):
    _smallest_difference(a_arr) # merge sort
    _smallest_difference(b_arr) # merge sort
    return _smallest_difference(a_arr + b_arr, midpoint=len(a_arr))