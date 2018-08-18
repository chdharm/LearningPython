from itertools import *
def allSubstring(s):
    for i in xrange(len(s)):
        for each in subseqs(s, i + 1):
            print each

if __name__=='__main__':
    print allSubstring('65237262323')