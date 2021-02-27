from threading import Thread

def sqaure_numbers():
    for i in range(100):
        i*i

if __name__ == '__main__':
    threads = []
    run_threads = 10

    #Create threads
    for i in range(run_threads):
        thread = Thread(target=sqaure_numbers)
        threads.append(thread)

    #Start threads
    for thread in threads:
        thread.start()

    #Join threads: nwait for them to complete

    for thread in threads:
        thread.join() #Blocking main thred until it completes

    print('end')