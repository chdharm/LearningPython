t = int(input())
while t > 0:
    t -= 1
    N = int(input())
    print(N*N)
    # complete_range = (2*N)+1
    # max_deviator = round(complete_range/3)
    # count = 0
    # # print("max_deviator:", max_deviator)
    # for i in range(1, max_deviator):
    #     for j in range(1, complete_range - i + 1, i):
    #         count += 1
    # print(count)