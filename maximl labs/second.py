def sort_by_char(s):
    return ''.join(sorted(s))


# def is_anagram(a, b):
#     if len(a) != len(b):
#         return False
#     a = sort_by_char(a)
#     b = sort_by_char(b)
#     if a != b:
#         return False
#     return True

b = ["abcd", "dbca", "xyz", "def", "zyx", "cadb", "aabcd", "ghi", "cabda", "abaa", "abba"]

if __name__ == '__main__':
    for index, value in enumerate(b):
        b[index] = (sort_by_char(value), value)
    dic = {}
    for value in b:
        if dic.get(value[0]) is not None:
            dic[value[0]].append(value[1])
        else:
            dic[value[0]] = []
    print("dic:", dic)

