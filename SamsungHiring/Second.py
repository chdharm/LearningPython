def sub_lists(list1):
    # store all the sublists
    sublist = [[]]

    # first loop
    for i in range(len(list1)):

        # second loop
        for j in range(i + 1, len(list1)):
            # slice the subarray
            sub = list1[i:j]
            sublist.append(sub)

    return sublist

if __name__=='__main__':
    n=input()
    for i in xrange(n):
        max=0
        size=input()
        li=map(int,raw_input().split())
        setsublist=sub_lists(li)
        #print setsublist
        l=len(setsublist)
        for i in xrange(l):
            isize=len(setsublist[i])
            if isize<2:
                continue
            if (setsublist[i][0]>=setsublist[i][isize-1]) and isize>max:
                max=isize
        print max
