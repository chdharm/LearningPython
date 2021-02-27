# from threading import Thread
#
#
# def square_numbers():
#     for i in range(1000):
#         result = i * i
#
#
# if __name__ == "__main__":
#     threads = []
#     num_threads = 10
#
#     # create threads and asign a function for each thread
#     for i in range(num_threads):
#         thread = Thread(target=square_numbers)
#         threads.append(thread)
#
#     # start all threads
#     for thread in threads:
#         thread.start()
#
#     # wait for all threads to finish
#     # block the main thread until these threads are finished
#     for thread in threads:
#         thread.join()
#


from threading import Thread
import time

# all threads can access this global variable
database_value = 0


def increase():
    global database_value  # needed to modify the global value

    # get a local copy (simulate data retrieving)
    local_copy = database_value

    # simulate some modifying operation
    local_copy += 1
    time.sleep(0.1)

    # write the calculated new value into the global variable
    database_value = local_copy


if __name__ == "__main__":
    print('Start value: ', database_value)

    t1 = Thread(target=increase)
    t2 = Thread(target=increase)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('end main')