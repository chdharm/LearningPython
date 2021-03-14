def custom_sorted(input, func):  # Going with selection sort
    len_input = len(input)
    dic = {} #Sort of remembering
    for index, value in enumerate(input):
        # print("value:", value)
        min_index = index
        if dic.get(value):
            min_score = dic.get(value)
        else:
            min_score = func(value)
            # min_score = value
        for adj_index in range(index + 1, len_input):
            # print("input[adj_index]:", input[adj_index])
            if dic.get(value):
                curr_score = dic.get(input[adj_index])
            else:
                # curr_score = input[adj_index]
                curr_score = func(input[adj_index])

            if curr_score < min_score:
                min_index = adj_index
                min_score = curr_score
        if min_index != index:
            input[min_index], input[index] = input[index], input[min_index]
    return input




if __name__ == '__main__':
    input_arry = [
        (5,3), (4,9), (1,3), (0,-3), (9,-3), (0, 0)
    ]
    # print(custom_sorted([-3,54,321,21,9,0,316533,367151331]))
    result = custom_sorted(input_arry, lambda x: x[0] * x[0] + x[1] * x[1])
    print("result:", result)
