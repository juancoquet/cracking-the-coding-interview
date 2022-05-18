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


# 16.7 number max
def number_max(a, b):
  diff = b - a
  sign = get_sign(diff)
  return a * sign + b * (1 - sign)

def get_sign(x):
    return (x & (1 << 63)) >> 63


# 16.8 'english int'
def english_int(n):
    if n == 0:
        return 'zero'

    units = {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }
    tens = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety',
    }
    teens = {
        0: 'ten',
        1: 'eleven',
        2: 'twelve',
        3: 'thirteen',
        4: 'fourteen',
        5: 'fifteen',
        6: 'sixteen',
        7: 'seventeen',
        8: 'eighteen',
        9: 'nineteen',
    }
    macros = {
        0: '',
        1: ' thousand, ',
        2: ' million, ',
        3: ' billion, ',
    }

    output = ''
    macro = 0

    while n > 0:
        last_three = n % 1000
        n = n // 1000
        if last_three == 0:
            continue

        digits = list(str(last_three))
        digits = [int(d) for d in digits]
        h, t, u = 0, 0, 0
        if digits:
            u = digits.pop()
        if digits:
            t = digits.pop()
        if digits:
            h = digits.pop()
        
        group = ''
        
        if h:
            group += units[h] + ' hundred '
        if t > 1:
            group += tens[t] + ' '
            group += units[u]
        elif t == 1:
            group += teens[u]
        elif t == 0:
            group += units[u]

        group += macros[macro]
        macro += 1
        
        output = group + output

    return output


# 16.9 'operations'
def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result += a
    if b < 0:
        return -result
    return result

def subtract(a, b):
    result = 0
    if b < a:
        while b < a:
            result += 1
            b += 1
    elif b > a:
        while a < b:
            result += 1
            a += 1
        result = -result
    return result

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    result = 0
    running_total = 0
    if a > 0:
        while running_total < a:
            result += 1
            running_total += abs(b)
        if b < 0:
            result = -result
    elif a < 0:
        while running_total > a:
            result += 1
            running_total = subtract(running_total, abs(b))
        if b > 0:
            result = -result
    return result