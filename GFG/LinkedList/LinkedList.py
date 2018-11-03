class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

if __name__=='__main__':
    llist=LinkedList()
    llist.head=Node(10)
    second=Node(20)
    third=Node(30)
    second.next=third
    llist.head.next=second

