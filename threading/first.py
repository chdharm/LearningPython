import threading

def countdown():
    x = 1000000000
    while x > 0:
        x -= 1


# Implementation 1: Multi-threading
def implementation_1():
    thread_1 = threading.Thread(target=countdown)
    thread_2 = threading.Thread(target=countdown)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()


# Implementation 2: Run in serial
def implementation_2():
    countdown()
    countdown()


if __name__ == '__main__':
    implementation_2()