# 10.2 group anagrams
def group_anagrams(strings):
    anagrams = {}
    while strings:
        s = strings.pop()
        anagrams[s] = []
        for s2 in strings:
            if is_anagram(s, s2):
                anagrams[s].append(s2)
                strings.remove(s2)
    result = []
    for key in anagrams.keys():
        result += [key]
        result += anagrams[key]
    return result

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    chars = {}
    for ch in s1:
        if not ch in chars:
            chars[ch] = 1
        else:
            chars[ch] += 1

    for ch in s2:
        if ch not in chars:
            return False
        chars[ch] -= 1
        if chars[ch] == 0:
            del chars[ch]

    if len(chars.keys()) > 0:
        return False
    return True

# solving 10.3 search in rotated sorted array
def search_rotated_array(a, target):
    splitpoint = 0
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            splitpoint = i
            break
    b = a[splitpoint:] + a[:splitpoint]
    target_found = bin_search(target, b)
    if target_found is not None:
        return (target_found + splitpoint) % len(a)
    else:
        return None

def bin_search(target, a, left_i=0):
    if len(a) == 0:
        return None
    midpoint = len(a) // 2
    if a[midpoint] == target:
        return midpoint + left_i
    if a[midpoint] < target:
        return bin_search(target, a[midpoint+1:], left_i=midpoint+1)
    else:
        return bin_search(target, a[:midpoint], left_i=left_i)


# 10.4 'sorted serach, no size'
class Listy(list):

    def __getitem__(self, i):
        try:
            return super().__getitem__(i)
        except IndexError:
            return -1


def get_size(listy):
    s = 1
    while listy[s] != -1:
        s *= 2
    return _get_size(listy, s//2, s)

def _get_size(listy, left, right):
    if left == right:
        return left + 1
    elif right - left == 1 and listy[right] == -1:
        return left + 1
    elif right - left == 1 and listy[right] != -1:
        return right + 1

    mid = (left + right) // 2
    found = listy[mid]
    if found == -1:
        return _get_size(listy, left, mid)
    else:
        return _get_size(listy, mid, right)

def bin_search(listy, x, left, right):
    mid = (left + right) // 2
    if listy[mid] == x:
        return mid
    if listy[mid] < x:
        return bin_search(listy, x, mid+1, right)
    if listy[mid] > x:
        return bin_search(listy, x, left, mid-1)

def search(listy, x):
    size = get_size(listy)
    return bin_search(listy, x, left=0, right=size-1)


# 10.5 sparse search
def sparse_search(target, a, left=0):
    mid = len(a) // 2
    if a[mid] == target:
        return mid + left
    if a[mid] != "":
        if a[mid] < target:
            return sparse_search(target, a[mid+1:], left=mid+left+1)
        if a[mid] > target:
            return sparse_search(target, a[:mid], left=left)
    else:
        l, r = (mid - 1, mid + 1)
        while a[l] == "" and a[r] == "":
            if l > 0:
                l -= 1
            if r < len(a) - 1:
                r -= 1
        if a[l]:
            mid = l
        elif a[r]:
            mid = r
        
        if a[mid] == target:
            return mid + left
        if a[mid] < target:
            return sparse_search(target, a[mid+1:], left=mid+left+1)
        if a[mid] > target:
            return sparse_search(target, a[:mid], left=left)


# 10.8 find duplicates
def find_duplicates(a):
    bv = 0
    for i in a:
        if get_bit(bv, i-1):
            print(i)
        else:
            bv = set_bit(bv, i-1)

def get_bit(num, i):
    mask = 1 << i
    return (num & mask) != 0

def set_bit(num, i):
    mask = 1 << i
    return num | mask


# soliving 10.10 'rank from stream'
def track(num, arr=[]):
    i = get_index(num, arr)
    return arr[:i] + [num] + arr[i:]

def get_rank(num, arr): # assuming num exists in arr
    i = get_index(num, arr)
    while arr[i] == num:
        i += 1
    return i -1

def get_index(num, arr, left_i=0):
    if len(arr) == 0:
        return left_i
    mid = len(arr) // 2
    if arr[mid] == num:
        return left_i + mid
        
    elif arr[mid] > num:
        return get_index(num, arr[:mid], left_i=left_i)
    elif arr[mid] < num:
        return get_index(num, arr[mid+1:], left_i=left_i+mid+1)


# 10.11 peaks and valleys
def peaks_and_valleys(arr):
    if len(arr) <= 2:
        return arr
    i = 1
    while i < len(arr) - 1:
        h, j = i-1, i+1
        max_idx = get_max_idx(arr, h, i, j)
        if i != max_idx:
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        i += 2
    return arr

def get_max_idx(arr, i, j, k):
    values = [arr[i], arr[j], arr[k]]
    biggest = max(values)
    which = values.index(biggest)
    return [i, j, k][which]