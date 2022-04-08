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