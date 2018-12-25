# def cost_char(c1,c2):
#     return abs(ord(c1)-ord(c2))
# def cost(s1,s2):
#     l=len(s1)
#     total=0
#     for i in xrange(0,l):
#         total+=cost_char(s1[i],s2[i])
#     return total
def LD(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    res = min([LD(s[:-1], t) + 1,
               LD(s, t[:-1]) + 1,
               LD(s[:-1], t[:-1]) + cost])
    return res
def cost(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]
if __name__=='__main__':
    str=raw_input()
    n=int(raw_input())
    str_len=len(str)
    main_str=str[0:n]
    total=0
    for i in range(n,str_len,n):
        total+=(LD(main_str,str[i:i+n]))
    print total





















    --------------------------


    def cost(s1, s2):
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        distances = range(len(s1) + 1)
        for i2, c2 in enumerate(s2):
            distances_ = [i2 + 1]
            for i1, c1 in enumerate(s1):
                if c1 == c2:
                    distances_.append(distances[i1])
                else:
                    distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
            distances = distances_
        return distances[-1]


    def LD(s, t):
        if s == "":
            return len(t)
        if t == "":
            return len(s)
        if s[-1] == t[-1]:
            cost = 0
        else:
            cost = 1

        res = min([LD(s[:-1], t) + 1,
                   LD(s, t[:-1]) + 1,
                   LD(s[:-1], t[:-1]) + cost])
        return res


    if __name__ == '__main__':
        str = raw_input()
        n = int(raw_input())
        str_len = len(str)
        main_str = str[0:n]
        total = 0
        for i in range(n, str_len, n):
            total += (LD(main_str, str[i:i + n]))
        print total
