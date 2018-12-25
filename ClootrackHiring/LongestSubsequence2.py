def maxLenSub( arr, n):
    arr.sort()
    mls=[]
    max = 0
    for i in range(n):
        mls.append(1)
    for i in range(n):
        for j in range(i):
            if (abs(arr[i] - arr[j]) <= 1 and mls[i] < mls[j] + 1):
                mls[i] = mls[j] + 1
    for i in range(n):
        if (max < mls[i]):
            max = mls[i]
    return max
if __name__ == '__main__':
    T = input()
    while T:
        T = T - 1
        N = input()
        li = []
        li=map(int,raw_input().split())
        print maxLenSub(li,N)
        #print longestSubseqWithDiffOne(li, N)
