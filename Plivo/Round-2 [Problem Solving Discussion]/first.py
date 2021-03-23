  #     1
  #   2    3
  # 4   5 6   7
  #

q = [6, 7]
len = 2
list = [2, 3]
from_left = True

Console - 1,

from_left = False
q = Queue()
q.push(root)
while not q.empty():
    ele = q.pop()
    print(ele.data)
    if root.left:
        q.push(root.left)
    if root.right:
        q.push(root.right)
    i = 0
    len_of_the_level = len(q)

    list = []
    for i in range(i, len_of_the_level):
        list.append(q.pop())

    if from_left:
        start = 0
        end = len_of_the_level-1
        increment = 1
    else:
        start = len_of_the_level - 1
        end = - 1
        increment = -1
    from_left = not from_left
    list2 = []
    for i in range(start, end , increment):
        print(list[i].data)
        list3 = []
        if list[i].left:
            list3.push(list[i].left)
        if list[i].right:
            list3.push(list[i].right)
        list3.extend(list2)
        list2 = list3
    for i in list2:
        q.push(i)



