def PrintPl(c):
    t1 = []
    for i in c:
        if i == "G":
            t1.append("C")
            continue
        elif i == "C":
            t1.append("G")
            continue
        elif i == "T":
            t1.append("A")
            continue
        elif i == "A":
            t1.append("U")
            continue
        else:
            print "Invalid Input"
            return
    print "".join(t1)
if __name__=='__main__':
    c=raw_input()
    PrintPl(c)
