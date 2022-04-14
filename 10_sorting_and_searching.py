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


a = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]