from heapq import merge


# 1.1 is unique
def is_unique(string):
    if len(string) > 128: # total ascii chars
        return False
    chars = {}
    for ch in string:
        if ch not in chars:
            chars[ch] = 1
        else:
            return False
    return True

# 1.2 check permutation
def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    chars = dict()
    for c in s1:
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    for c in s2:
        if c not in chars:
            return False
        chars[c] -= 1
        if chars[c] == 0:
            del chars[c]
    if len(chars.keys()) == 0:
        return True
    return False

# 1.3 URLify
def urlify(s):
	s = s.rstrip()
	s = s.replace(' ', '%20')
	return s