from threading import Thread, Lock, active_count, current_thread, get_ident,
enumerate,
from time import sleep

database_count = 0

def increase():
    global database_count
    local_count = database_count
    sleep(1)
    local_count += 1
    database_count = local_count

database_count_2 = 0
def increase_2(lock):
    global database_count_2
    lock.acquire()
    local_count = database_count_2
    sleep(1)
    local_count += 1
    database_count_2 = local_count
    lock.release()

database_count_3 = 0
def increase_3(lock):
    with lock:
        global database_count_3
        local_count = database_count_3
        sleep(1)
        local_count += 1
        database_count_3 = local_count

if __name__ == '__main__':
    print('------Start------')
    t1 = Thread(target=increase)
    t2 = Thread(target=increase)
    print("count-1:::", database_count)
    print("active_count-1:::", active_count())
    t1.start()
    t2.start()
    print("active_count-2:::", active_count())
    t1.join()
    t2.join()
    print("count-2:::", database_count)

    lock = Lock()
    print("active_count-3:::", active_count())
    t3 = Thread(target=increase_2, args=(lock,))
    t4 = Thread(target=increase_2, args=(lock,))
    print("count-3:::", database_count_2)
    t3.start()
    t4.start()
    print("active_count-4:::", active_count())
    t3.join()
    t4.join()
    print("count-4:::", database_count_2)

    t5 = Thread(target=increase_3, args=(lock,))
    t6 = Thread(target=increase_3, args=(lock,))
    print("count-5:::", database_count_3)
    print("active_count-5:::", active_count())
    t5.start()
    t6.start()
    print("active_count-6:::", active_count())
    t5.join()
    t6.join()
    print("active_count-7:::", active_count())
    print("count-6:::", database_count_3)