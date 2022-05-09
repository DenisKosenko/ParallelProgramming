import threading
import time


def func_1():
    print("func_1 in progress...")
    time.sleep(10)
    print("func_1 - finish.")

def func_2():
    print("func_2 in progress...")
    time.sleep(5)
    print("func_2 - finish.")

def main():
    th1 = threading.Thread(target=func_1)
    th2 = threading.Thread(target=func_2)
    th1.start()
    th1.join()
    th2.start()
    th2.join()


if __name__ == "__main__":
    main()