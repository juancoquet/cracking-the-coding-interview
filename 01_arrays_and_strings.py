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

# 1.4 Palindrome Permutation
def palindrome_permutation(input_text):
    input_text = input_text.replace(' ', '')
    chars = []
    for c in input_text:
        if not c in chars:
            chars.append(c)
        else:
            chars.remove(c)
    return len(chars) <= 1

# 1.5 One Away
def char_inserted(s1, s2):
    if len(s2) != len(s1) + 1:
        return False
    for i, c in enumerate(s1):
        if c != s2[i]:
            break
    else:
        i += 1
    if i < len(s2) - 1:
        s3 = s2[:i] + s2[i+1:]
    else:
        s3 = s2[:-1]
    return s1 == s3

def char_deleted(s1, s2):
    if len(s2) != len(s1) - 1:
        return False
    for i, c in enumerate(s2):
        if c != s1[i]:
            break
    else:
        i += 1
    if i < len(s1) - 1:
        s3 = s1[:i] + s1[i+1:]
    else:
        s3 = s1[:-1]
    return s2 == s3

def char_replaced(s1, s2):
    if len(s1) != len(s2):
        return False
    for i, c in enumerate(s1):
        if c != s2[i]:
            break
    else:
        return False
    if i < len(s1) - 1:
        s1 = s1[:i] + s1[i+1:]
        s2 = s2[:i] + s2[i+1:]
    else:
        s1 = s1[:-1]
        s2 = s2[:-1]
    return s1 == s2

def one_away(s1, s2):
    if s1 == s2:
        return True
    return char_inserted(s1, s2) or char_deleted(s1, s2) or char_replaced(s1, s2)


# 1.6 string compression
def string_compression(s):
    length = len(s)
    compressed = ''
    current_char = s[0]
    count = 0
    for c in s:
        if c != current_char:
            compressed += current_char + str(count)
            current_char = c
            count = 1
            if len(compressed) >= length:
                return s
        else:
            count += 1
    compressed += current_char + str(count)
    return compressed


# 1.7 rotate matrix
import copy

def rotate(matrix):
    n = len(matrix)
    m_copy = copy.deepcopy(matrix)

    col = n - 1
    for row in matrix:
        for r in m_copy:
            r[col] = row.pop(0)
        col -= 1
    return m_copy


# 1.8 zero matrix
def zero_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[r] = [0 for _ in matrix[r]]
                for row in matrix:
                    row[c] = 0
                break
    return matrix