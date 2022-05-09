import ctypes

result = ctypes.windll.user32.MessageBoxW(0, "Choose something", "window", 3)

if result == 6:
    print("user pressed yes")
elif result == 7:
    print("user pressed no")
elif result == 2:
    print("user pressed cancel")
else:
    print("unknown return code")