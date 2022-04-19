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