import threading

#子线程死循环
def abc():
    while True:
        pass

t1 = threading.Thread(target=abc)
t1.start()

#主线程死循环
while True:
    pass