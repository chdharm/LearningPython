import multiprocessing
import time


def square(x):
    return x * x


if __name__ == '__main__':
    print("________1_________")
    pool = multiprocessing.Pool()
    inputs = [0, 1, 2, 3, 4]
    outputs_async = pool.map_async(square, inputs)
    print(outputs_async)
    print("outputs_async: {}".format(outputs_async))
    outputs = outputs_async.get()
    print("Output: {}".format(outputs))

    print("________2_________")

    pool = multiprocessing.Pool()
    result_async = [pool.apply_async(square, args=(i,)) for i in
                    range(10)]
    results = [r.get() for r in result_async]
    print("Output: {}".format(results))