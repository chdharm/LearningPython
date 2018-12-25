def longestSubseqWithDiffOne(li, n):
    dp = [1 for i in range(n)]
    for i in range(n):
        for j in range(i):
            if ((li[i] == li[j] + 1) or (li[i] == li[j] - 1)):
                dp[i] = max(dp[i], dp[j] + 1)
    result = 1
    for i in range(n):
        if (result < dp[i]):
            result = dp[i]
    return result+1
if __name__ == '__main__':
    T = input()
    while T:
        T = T - 1
        N = input()
        li = []
        li=map(int,raw_input().split())
        print longestSubseqWithDiffOne(li, N)
