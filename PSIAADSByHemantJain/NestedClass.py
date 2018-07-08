class LinkedList:
    class Node:
        def __init__(self,v,n=None):
            self.value=v
            self.next=n
    def __init__(self):
        self.head=None