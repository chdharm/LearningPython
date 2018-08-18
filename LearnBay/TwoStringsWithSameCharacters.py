#########################Done#########################
#First Aproach
def IsSame(s1,s2):
    l1=len(s1)
    l2 = len(s2)
    if l1!=l2:
        return False
    if l1<1 and l2<1:
        return True
    if l1<1 or l2<1:
        return False
    #We can sort then and compare character by character

#Second Approach
def IsSame2(s1,s2):
    #I will  do it using an array where we will store the count of
    #of characters using ascii value of the character
    pass

# Third Approach
def IsSame3(s1, s2):
    # I will  do it using dictionary for strong count for first string
    #Will check second string char and decrease the count : if we will get any charcter not existing in dict keys then return false
    #At the end of our operation if any count is greater than zero then retun false
    pass

if __name__=='__main__':
    s1 = input()
    s2 = input()
    print IsSame(s1,s2)