def get_max_subarray_sum(input_li):
    global_max = -10000000
    local_max = 0
    for i in input_li:
        local_max += i
        if local_max < 0:
            local_max = 0
        if global_max < local_max:
            global_max = local_max
    return global_max

if __name__ == '__main__':
    li = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    print(get_max_subarray_sum(li))
