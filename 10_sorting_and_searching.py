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

unordered_anagrams = ['abc', 'def', 'ghi', 'cab', 'gef', 'hig']
print(group_anagrams(unordered_anagrams))