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


# 17.6 count of twos
# brute force
def count_of_twos_a(n):
    twos = 0
    for num in range(n+1):
        digits = list(str(num))
        twos += digits.count('2')
    return twos

# optimised
def digit_at_i(num, i):
    for _ in range(i):
        num = num // 10
    return num % 10
    
def twos_at_i(num, i):
    twos = 0
    digit = digit_at_i(num, i)

    round_down = num - num % 10**(i+1)
    round_up = round_down + 10**(i+1)
    right_of_i = num % 10**i

    if digit < 2:
        twos += round_down / 10
    elif digit > 2:
        twos += round_up / 10
    elif digit == 2:
        twos += round_down / 10 + right_of_i + 1

    return twos

def count_of_twos_b(num):
    n = num
    num_digits = 0
    while n > 0:
        num_digits += 1
        n = n // 10

    twos = 0

    for i in range(num_digits):
        twos += twos_at_i(num, i)

    return int(twos)


# 17.7 baby names
def baby_names(names, synonyms):
    name_synonyms = {}
    
    for n1, n2 in synonyms:
        # add keys if don't exist
        if n1 not in name_synonyms:
            name_synonyms[n1] = []
        if n2 not in name_synonyms:
            name_synonyms[n2] = []

        # get already existing syns
        n1_syns = name_synonyms[n1][:]
        n2_syns = name_synonyms[n2][:]

        # add n2 to n1
        if not n2 in name_synonyms[n1]:
            name_synonyms[n1].append(n2)
        # add n1 to n2
        if not n1 in name_synonyms[n2]:
            name_synonyms[n2].append(n1)

        # add n2 to all other syns of n1	
        for syn in n1_syns:
            if n2 not in name_synonyms[syn]:
                name_synonyms[syn].append(n2)
            # add syns of n1 to n2
            if syn not in name_synonyms[n2]:
                name_synonyms[n2].append(syn)
        # add n1 to all other syns of n2
        for syn in n2_syns:
            if n1 not in name_synonyms[syn]:
                name_synonyms[syn].append(n1)
            # add syns of n2 to n1
            if syn not in name_synonyms[n1]:
                name_synonyms[n1].append(syn)

    freq = {}
    for name in name_synonyms.keys():
        freq[name] = 0

    for name, count in names:
        if not name in freq:
            freq[name] = count
        else:
            freq[name] += count
            syns = name_synonyms[name]
            for syn in syns:
                freq[syn] += count

    while len(name_synonyms) > 0:
        first = [k for k in name_synonyms.keys()][0]
        syns = name_synonyms[first]
        for s in syns:
            del name_synonyms[s]
            del freq[s]
        del name_synonyms[first]

    return freq


# 17.9 kth multiple
from math import sqrt, ceil


def erastothenes(n):
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, ceil(sqrt(n))):
        for multiple in range(i**2, n, i):
            is_prime[multiple] = False
    
    return [i for i in range(n) if is_prime[i]]

def check_prime_factors(n):
    if n % 2 == 0:
        return False
    primes = erastothenes(n+1)
    try:
        primes.remove(3)
        primes.remove(5)
        primes.remove(7)
    except ValueError:
        pass
    if n in primes:
        return False

    for prime in primes:
        if n % prime == 0:
            return False
    return True

def kth_multiple(k):
    found_multiples = 0
    i = 1
    while found_multiples < k:
        if check_prime_factors(i):
            found_multiples += 1
        i += 1
    return i - 1


# 17.10 'majority element'
def check_sub_array(arr, start):
    item = arr[start]
    count = 1
    i = start + 1
    while count > 0 and i < len(arr):
        if arr[i] == item:
            count += 1
        else:
            count -= 1
        i += 1
    if count > 0:
        return (True, i)
    return (False, i)

def validate(arr, i):
    item = arr[i]
    count = 0
    for elem in arr:
        if elem == item:
            count += 1
        else:
            count -= 1
    if count > 0:
        return item
    return -1

def majority_element(arr):
    i = 0
    while i < len(arr):
        check = check_sub_array(arr, i)
        if check[0] == True:
            if (maj_el := validate(arr, i)) != -1:
                return maj_el
        last_checked = check[1]
        i = last_checked + 1
    return -1