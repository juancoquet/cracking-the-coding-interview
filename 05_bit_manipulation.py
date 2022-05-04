def get_bit(num, i):
    mask = 1 << i
    return (num & mask) != 0

def set_bit(num, i):
    mask = 1 << i
    return num | mask

def clear_bit(num, i):
    mask = ~(1 << i)
    return num & mask


def next_biggest(bits):
    if bits == 0:
        raise ValueError('0 is not a valid input')
    i = 0
    while not get_bit(bits, i):
        i += 1

    bits = clear_bit(bits, i)
    i += 1
    
    while get_bit(bits, i):
        i += 1

    bits = set_bit(bits, i)

    return bits

def next_smallest(bits):
    if bits <= 1:
        raise ValueError('Input must be greater than 1')
    i = 1
    while not get_bit(bits, i):
        i += 1
    one_index = i
    
    while get_bit(bits, i):
        i -= 1
        if i < 0:
            raise ValueError('No smaller binary int exists with the same number of 1s')
    zero_index = i
    bits = clear_bit(bits, one_index)
    bits = set_bit(bits, zero_index)
    return bits

# 5.4 next number
def next_number(bits):
    bigger = next_biggest(bits)
    smaller = next_smallest(bits)
    return bigger, smaller


# 5.6 conversion
def converstion(a, b):
    if a == b:
        return 0
    length = max([a.bit_length(), b.bit_length()])
    count = 0
    for i in range(length):
        if get_bit(a, i) != get_bit(b, i):
            count += 1
    return count

def get_bit(num, i):
    mask = 1 << i
    return num & mask != 0


# 5.7 pairwise swap
def get_bit(num, i):
    mask = 1 << i
    return (num & mask) != 0

def set_bit(num, i):
    mask = 1 << i
    return num | mask

def clear_bit(num, i):
    mask = ~(1 << i)
    return num & mask

def pairwise_swap(num):
    length = num.bitlength()
    for i in range(length, 2):
        b1 = get_bit(num, i)
        b2 = get_bit(num, i+1)
    if b1 and not b2:
        clear_bit(num, i)
        set_bit(num, i+1)
    if b2 and not b1:
        clear_bit(num, i+1)
        set_bit(num, i)


# 5.8 draw line
def get_byte_index(x, y, bpl):
    start_of_line = (y - 1) * bpl
    return int(start_of_line + x // 8)

def get_bit_index(x):
    return int(8 - x % 8)

def draw_line(arr, w, x1, x2, y):
    h = len(arr) * 8 / w
    bytes_per_line = len(arr) // h
    
    start_byte = get_byte_index(x1, y, bytes_per_line)
    start_bit = get_bit_index(x1)
    start_mask = (1 << (start_bit + 1)) - 1
    arr[start_byte] = arr[start_byte] | start_mask

    end_byte = get_byte_index(x2, y, bytes_per_line)
    end_bit = get_bit_index(x2)
    ones = 0xFF
    end_mask = ((1 << end_bit) - 1) ^ ones
    if start_byte != end_byte:
        arr[end_byte] = arr[end_byte] | end_mask
    else:
        mask = start_mask & end_mask
        arr[end_byte] = arr[end_byte] & mask

    for i in range(start_byte + 1, end_byte):
        arr[i] = arr[i] | ones

    return arr