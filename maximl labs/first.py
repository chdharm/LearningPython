def sort_by_char(s):
    return ''.join(sorted(s))


def is_anagram(a, b):
    if len(a) != len(b):
        return False
    a = sort_by_char(a)
    b = sort_by_char(b)
    if a != b:
        return False
    return True

b = ["abcd", "dbca","xyz", "def", "zyx", "cadb", "aabcd", "ghi", "cabda", "abaa", "abba"]

if __name__ == '__main__':
    len_b = len(b)
    for index, i in enumerate(b):
        anagrams = []
        if i == '-1':
            continue
        for j in range(index+1, len_b):
            if b[j] == '-1':
                continue
            is_ag = is_anagram(i, b[j])
            if is_ag:
                anagrams.append(b[j])
                b[j] = '-1'
        print("Anagram of {} is {}.".format(str(i), ' '.join(anagrams) ))