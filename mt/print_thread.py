import threading
from threading import Thread


class PrintThread(Thread):
    def run(self):
        print(threading.current_thread())
        for n in range(1, 11):
            print(n)


t1 = PrintThread()
t1.start()   # Call run()
print(threading.current_thread())