if __name__=="__main__":
    st=raw_input()
    #print st
    vowels=['a','e','i','o','u']
    for i in st.lower():
        if i in vowels:
            st=st.replace(i,'')
    print st