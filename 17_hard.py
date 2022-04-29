import math

# 17.1 Add without plus
def add_without_plus(a, b):
    bit_length = max(a.bit_length(), b.bit_length())
    carry = False
    result = 0
    for i in range(bit_length + 1):
        a_bit = get_bit(a, i)
        b_bit = get_bit(b, i)
        added = a_bit ^ b_bit
        if carry:
            added = added ^ 1
        if (a_bit and b_bit) or ((a_bit != b_bit) and carry):
            carry = True
        else:
            carry = False
        if added == 1:
            result = set_bit(result, i)
    return result
        

def get_bit(num, i):
    mask = 1 << i
    if num & mask != 0:
        return 1
    else:
        return 0

def set_bit(num, i):
    return num | (1 << i)

# 17.2 shuffle
import random

def shuffle(deck):
    shuffled = []
    while len(deck) > 0:
        i = random.randrange(0, len(deck))
        card = deck.pop(i)
        shuffled.append(card)
    return shuffled


# 17.4 missing number
def missing_number(a):
    n = len(a) + 1
    bits = math.ceil(math.log(n, 2))
    nums = {}
    
    for item in a:
        num = 0
        for i in range(bits):
            bit = get_bit(item, i)
            num += bit * (2**i)
        nums[num] = True
    
    for num in range(n):
        if nums.get(num) is None:
            return num

# 17.5 letters and numbers
def letters_and_numbers(a):
    letters, numbers = 0, 0
    diffs = [0]
    for item in a:
        if type(item) is str:
            letters += 1
        if type(item) is int:
            numbers += 1
        diffs.append(letters - numbers)

    first_appeared = {}
    longest_sub = []
    
    for i, diff in enumerate(diffs):
        if not diff in first_appeared:
            first_appeared[diff] = i
        else:
            sub_length = i - first_appeared[diff]
            if sub_length > len(longest_sub):
                start = first_appeared[diff]
                longest_sub = a[start:i]
    return longest_sub

a = [0, 0, 0, 0, 0, 'a', 1, 'b', 2, 'c', 3, 4, 5, 6, 'd']

print(letters_and_numbers(a))