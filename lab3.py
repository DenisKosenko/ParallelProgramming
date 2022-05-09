import threading
import time


def func_1():
    print("func_1 in progress")
    event.wait()
    time.sleep(2)
    print("func_1 started")

    event.set()

    for i in range(len(nums)):
        nums[i] = (nums[i] + 10) * 2
    print(nums)

    event.clear()


def func_2():
    print("func_2 started")
    event.set()

    for i in range(len(nums)):
        nums[i] = nums[i] % 3
    print(nums)

    event.clear()


def func_3():
    print("func_3 in progress")
    event.wait()
    time.sleep(2)

    event.set()

    print("func_3 started")

    for i in range(len(nums)):
        nums[i] = nums[i] / 3
    print(nums)

    event.clear()


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(f"{nums}\n")

    event = threading.Event()

    th1 = threading.Thread(target=func_1)
    th2 = threading.Thread(target=func_2)
    th3 = threading.Thread(target=func_3)

    th1.start()
    th2.start()
    th3.start()

    th1.join()
    th2.join()
    th3.join()

