import threading, time

mutex = threading.Lock()

def thread_one():
    global mutex
    print("The first stream now sleeps for 5 seconds")
    time.sleep(5)
    print("First stream is finished")
    mutex.release()


def thread_two():
    global mutex
    print("The second stream now sleeps for 2 seconds")
    time.sleep(2)
    mutex.acquire()
    print("Second stream is finished")


mutex.acquire()
t1 = threading.Thread(target=thread_one)
t2 = threading.Thread(target=thread_two)
t1.start()
t2.start()