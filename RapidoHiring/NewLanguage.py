if __name__=='__main__':
    n=input()
    for _ in xrange(n):
        st=raw_input()
        if '+' in st:
            print "addition"
            a,b=st.split('+')
            print a,b
        elif '-' in st:
            print "subtraction"
            a, b = st.split('-')
            print a, b
        elif '/' in st:
            print "division"
            a, b = st.split('/')
            print a, b
        elif '*' in st:
            print "multiplication"
            a, b = st.split('*')
            print a, b