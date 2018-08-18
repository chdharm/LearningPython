try:
    raise ArithmeticError
    # strr=""
    # print "type of strr at loc. 1=",type(strr)
    # strr=input()
    # print "type of strr at loc. 2=", type(strr)
except ArithmeticError:

    print "Sorry Infinite"
else:
    print "inside else block"
finally:
    print "finally we met"