def first_approach_3(arr,):
    pass

def first_approach_4(arr,):
    pass

def is_adjacent(dic, num1, num2):
    if num1 == num2:
        #See if we have the two index no adjacent

    dic_val1 = dic[num1]
    dic_val2 = dic[num1]
    #Check if these two arrays have atleat one combination where difference is zero

def first_approach_5(arr):
    dic  = {}
    for index in range(0, len(arr)):
        if dic.get(arr[index]):
            dic[index].append(index)
        else:
            dic[index] = index
    sorted_arr = arr.sorted()
    for i in range(0, 3):
        for j in range(i + 1, 4):
            if not is_adjacent(dic, arr[i], arr[j]):
                return [i, j]







if __name__ == '__main__':
    arr = [2,3,5,7,8,7]
    print(first_approach_5(arr))
