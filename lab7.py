import ctypes
import threading


def thread1():
    ctypes.windll.user32.MessageBoxW(0, "1 thread started", "window", 0)
def thread2():
    ctypes.windll.user32.MessageBoxW(0, "2 thread started", "window", 0)

result = ctypes.windll.user32.MessageBoxW(0, "Select to run 1 thread and no to run 2 threads", "window", 3)

if result == 6:
    print("user pressed yes")
    t1 = threading.Thread(target=thread1)
    t1.start()
elif result == 7:
    print("user pressed no")
    t2 = threading.Thread(target=thread2)
    t2.start()
elif result == 2:
    print("user pressed cancel")
else:
    print("unknown return code")