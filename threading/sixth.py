import threading
import time

def func():
    print('ran')
    time.sleep(1)
    print('done')

x = threading.Thread(target=func, args=())
print(threading.activeCount())
x.start()
print("Hi")
print(threading.activeCount())
# x.()
# print(threading.activeCount())