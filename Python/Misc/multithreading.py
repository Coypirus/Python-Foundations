# Multithreading

from time import sleep
from threading import *

class Hello(Thread): # To make another thread the class must be subclass of Thread
    def run(self): # Run overrides a run() method in the Thread class
        for i in range(10):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start() # This will call the run method of a new thread(separate from main thread)
sleep(0.2)
t2.start() # This will call the run method of another new thread(also separate from main thread)

#Collision - two threads going to cpu at the same time.

t1.join()
t2.join()
print("Bye")