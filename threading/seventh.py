import threading
import time


def count(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.01)

if __name__ == '__main__':
    x = threading.Thread(target=count, args=(10,))
    y = threading.Thread(target=count, args=(10,))
    x.start()
    y.start()
    print("Done")